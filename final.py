def main_game():
    #Main Game:

    #Initialize the variables
    game_board = ["-" for i in range(10)] #this sets up a list of 9 "-"
    player_type = ""
    player_position = 0
    turn_count = 0

    #Print Opening text
    print_opening()

    #Print out the starting game board.
    print_board(game_board)


    #Main gameplay loop.  This will loop for 9 turns.
    #Each turn consists of:
    #   user input Position and error check
    #   user input X or O and error check
    #   print the gameboard so far
    #   check for a winner
    #   check to see if end of game (and issue draw if no winner and end)
    #   increase play counter
    while turn_count < 9:
        #Player Position input and error check
        player_position = error_check_pos(input("Select a playing position(1-9):"), game_board)

        #Player XO input and error check
        player_type = error_check_type(input("Select 'X' or 'O':").upper())

        #enter the player turn into the gameboard list tracker
        game_board[player_position-1] = player_type

        #Display Game board:
        print_board(game_board)

        winner = winner_check(game_board, player_type)

        #checks to see if there's a winner
        if winner:
            break

        #increase the play counter
        turn_count+=1

        #no winner on last turn, print out the draw message
        if turn_count == 9:
            print("No winner, game is a draw!")
            break


def print_opening():
    #Display the opening portion of the program.
    input('''
    IME-211-001 - Final Exam Program.
    By <Insert your name here>
    Due: March 23, 2023

    WELCOME TO THE GAME OF TIC TAC TOE

    This is a classic version fo the 2 player Tic Tac Toe game that dates back
    to ancient Egypt.

    Rules of the Game:

    One of the player's chooses "O" and the other chooses "X" to mark their
    respective calls. In order to win the game, a player must place three of their
    marks (all "O"'s or all "X"'s) in the horizontal, vertical, or diagnoal row.
    If no one wins, then the game is said to be a draw.

    Press any key to start the game...
    ''')

    
def error_check_pos(player_position, game_board):
    #initialize logic booleans
    stay_bool = True
    int_bool = False
    warn1_str = "Sorry that is not a valid playing position!"
    warn2_str = "Sorry, this position has already been selected!"
    retry_str = "Select another playing position from 1-9:"
    while stay_bool:
        # Make sure that the item entered is a number and won't break the
        # the int() functino. So this will catch entries that are like 5x
        # and other strings that cannot be converted to an int.
        int_bool = False
        while not int_bool:
            try:
                player_position = int(player_position)
                int_bool = True
            except ValueError:
                print(warn1_str)
                player_position =input(retry_str)

        #This block of text checks that the player position isn't outside
        #the playing range and makes sure it's not in a position that
        #has already been played.
        #also have to error check each value reentered so have to do the int
        #check again for each other error.
        int_bool = False
        if player_position < 1 or player_position > 9:
            print(warn1_str)
            player_position = input(retry_str)
            while not int_bool:
                try:
                    player_position = int(player_position)
                    int_bool = True
                except ValueError:
                    print(warn1_str)
                    player_position = input(retry_string)
        elif game_board[player_position-1] != "-":
            print(warn2_str)
            player_position = input("Select another playing position from 1-9:")
            while not int_bool:
                try:
                    player_position = int(player_position)
                    int_bool = True
                except ValueError:
                    print(warn1_str)
                    player_position = input(retry_str)
        else:
            stay_bool = False

    #returns the error checked player_position to the main loop
    return player_position

def error_check_type(player_type):
    #initalize the logic boolean
    stay_bool = True

    #this will check to ensure the user intput is an X or an O
    while stay_bool:
        if player_type == "X" or player_type == "O":
            stay_bool = False
        else:
            print("ERROR: Invalid Selection!")
            player_type = input("Please select an 'X' or 'O':").upper()

    #returns the error checked player_type
    return player_type


def winner_check(game_board, player_type):
    #Keep Tracking of the winning combos
    horizontals = [game_board[0:3], game_board[3:6], game_board[6:9]]
    verticals = [game_board[0:7:3],game_board[1:8:3], game_board[2::3]]
    diagnoals = [game_board[0::4], game_board[2:7:2]]

    #Check for winner:
    for i in horizontals:
        if "-" not in i:
            if "X" in i and "O" in i:
                continue
            else:
                print("{} player wins horizontally!".format(player_type))
                return True

    for i in verticals:
        if "-" not in i:
            if "X" in i and "O" in i:
                continue
            else:
                print("{} player wins vertically!".format(player_type))
                return True

    for i in diagnoals:
        if "-" not in i:
            if "X" in i and "O" in i:
                continue
            else:
                print("{} player wins diagnoally".format(player_type))
                return True

def print_board(game_board):
    #this will print out the formatted gameboard with the current
    #status of the game_board list
    print('''
                Tic Tac Toe
                {}|{}|{}
                {}|{}|{}
                {}|{}|{}

            '''.format(game_board[0], game_board[1], game_board[2],
                       game_board[3], game_board[4], game_board[5],
                       game_board[6], game_board[7], game_board[8]))


main_game()
