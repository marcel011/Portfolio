How to get this running in PyCharm:

    1. Install all of the dependencies shown in python_packages.png(You probably don't need all of them
    but I forgot which ones I was using.

    2. -In one of the top right drop down menus, click Edit Configurations.
       -On the top left, click + >> python.
       -See edit_configurations.png to help fill out the parameters
            script: /directory/to/manage.py
            Parameters: socketserver --debug --reload
            
    3. Create a file named settings.py in the root directory and put one line of code in it:
        SECRET_KEY = '8qEDQnVJ7JiyYZuNgq8mZfdK7S9LZLTe'
        
    4. If all goes to plan you can hit the run button and an internal server will be set up on your local machine pointing to        something like http://127.0.0.1:5000. Go there and play the battleship game.
