import flask
from flask import Flask
import base64
import uuid
import os
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# initiate socket.io
socketio = SocketIO(app)
recip_sockets = {}

games = {}
userList = {}
num_players = {}
room_players = {}


@app.before_request
def setup_csrf():
    if 'csrf_token' not in flask.session:
        flask.session['csrf_token'] = base64.b64encode(os.urandom(32)).decode('ascii')
    if 'auth_user' not in flask.session:
        flask.session['auth_user'] = base64.b64encode(os.urandom(32)).decode('ascii')
    if 'game_name' not in flask.session:
        flask.session['game_name'] = '0'
    if 'key' not in flask.session:
        flask.session['key'] = '0'
    if 'room' not in flask.session:
        flask.session['room'] = '0'


@app.route('/')
def index():
    return flask.render_template('index.html', games=games, num_players=num_players)


@app.route('/new-game', methods=['POST'])
def chat():
    game_name = flask.request.form['game_name']
    flask.session['game_name'] = game_name
    # store the game_name
    if game_name not in games:
        key = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:12].decode('ascii')
        games[game_name] = key
        flask.session['key'] = key
    else:
        key = games[game_name]
        flask.session['key'] = key

    if key not in userList:
        userList[key] = list()

    if key not in num_players:
        num_players[key] = 0

    if key not in room_players:
        room_players[key] = list()

    return flask.redirect('/'+key, code=303)


@app.route('/<string:key>')
def room(key):

    found = False
    # see if key exists
    for chat in games:
        if games[chat] == key:
            flask.session['game_name'] = chat
            flask.session['key'] = key
            found = True

    if not found:
        return flask.render_template('index.html', state='not_found')

    if flask.session['auth_user'] in room_players[key]:
        for name in games.copy():
            if games[name] == room:
                del games[name]
        return flask.render_template('index.html', state='bad')
    else:
        room_players[key].append(flask.session['auth_user'])

    if key in userList:
        if userList[key] is not None:
            users = userList[key]
        if userList[key] is None:
            return flask.redirect(flask.url_for('index'))

    if key not in userList:
        return flask.redirect(flask.url_for('index'))  # if no key, we bail to the index page :)

    if num_players[key] == 2:
        return flask.redirect(flask.url_for('full', key=key))

    name = flask.session['auth_user']
    game_name = flask.session['game_name']

    num_players[key] += 1
    player = num_players[key]
    return flask.render_template('game.html', key=key, sid=flask.session['csrf_token'],
                                 state='!joined', game_name=game_name,
                                 name=name, users=users, player=player, )


@app.route('/winner/<string:player>')
def you_win(player):
    winner = player
    sesh = flask.session['game_name']
    key=flask.session['key']
    return flask.render_template('you_win.html', winner=winner, session=sesh, key=key)


@app.route('/loser/<string:player>')
def loser_page(player):
    loser = player
    sesh = flask.session['game_name']
    key = flask.session['key']
    return flask.render_template('you_lost.html', loser=loser, session=sesh, key=key)


@app.route('/full/<string:key>')
def full(key):
    return flask.render_template('full.html', key=key, games=games, num_players=num_players)


@socketio.on('chat')
def chat(data):
    user_message = data['name'] + ': ' + data['_message']
    flask.session['room'] = data['room']
    emit('new-message', user_message, broadcast=True, room=flask.session['room'])


@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    username = data['username']
    flask.session['room'] = room
    if username == '-987jkl':
        return  # -987jkl is the default user name. we don't wanna do anything.
    username = data['username']
    flask.g.user = username
    flask.session['auth_user'] = username
    join_room(room)
    flask.session['session'] = data['sid']
    userList[room].append(username)
    emit("new-user", username, broadcast=True, room=room)


@socketio.on('leave')
def on_leave(data):
    print('INSIDE_LEAVE')
    room = data['room']
    leave_room(room)
    username = data['username']
    print('in leave function room: ' + room + ' username: ' + username)

    # delete the room.
    for name in games.copy():
        print('name: ' + name)
        if games[name] == room:
            print('deleting game')
            del games[name]

    userList[room].remove(username)
    user_message = 'Sever: ' + username + ' has left the chat.'
    emit('new-message', user_message, broadcast=True, room=flask.session['room'])
    emit('remove-user', username, broadcast=True, room=flask.session['room'])


@socketio.on('move')
def move(data):
    flask.session['room'] = data['room']
    flask.session['curr_player'] = data['curr_player']
    flask.session['sid'] = data['sid']

    emit('move', data, broadcast=True, room=data['room'])


@socketio.on('p2_join')
def p2_join(data):
    emit('p2-join', data, broadcast=True, room=flask.session['key'])


@socketio.on('disconnect')
def leave():
    leave(room)


if __name__ == '__main__':
    socketio.run(app)
