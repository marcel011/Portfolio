#  modified script from M. Ekstrand
import sys
from flask_script import Manager

import battleship as app_module
app = app_module.app


if hasattr(app_module, 'manager'):
    manager = app_module.manager
else:
    manager = Manager(app)

@manager.command
def socketserver(debug=False, reload=False):
    if hasattr(app_module, 'socketio'):
        sio = app_module.socketio
        sio.run(app, debug=debug, use_reloader=reload)
    else:

        sys.exit(1)


if __name__ == '__main__':
    manager.run()