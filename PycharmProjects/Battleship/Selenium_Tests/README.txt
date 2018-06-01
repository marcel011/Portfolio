Description of acceptance test cases:

Selenium IDE was used to test our Web Based Game.

The Selenium IDE is a Firefox plugin that will simulate a user's typing and clicking within a browser and run tests
to verify that everything was loaded correctly.

Part I user simulation:
    1. Selenium will automatically create a game room named "testroom".
    2. It will automatically sign in as the user "Magic Man".
    3. It will place all of player 1's game pieces on the board.
    4. It will type a chat message "testing chat!".

Part II testing:
    1. Selenium will verify that all 5 boats are visible on the page.
    2. It will assert if the text "Magic man: testing chat!" is in the chat room.
    3. It will verify that the game directions is displaying "Player 2: Pick 5 Spaces for your Carrier".
    4. It will verify if the footer, left board, and right board have been properly loaded.
    5. It will assert all Battleships for player 1 and 2 are displaying "Good" status on their ships


