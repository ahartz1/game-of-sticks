import random


def game_type():
    '''Asks user who they would like to play against and returns the corresponding
       number.
        [1] Another player
        [2] AI
        [3] Trained AI
    '''
    while True:
        game_type = input("Would you like to play against (1) Another Player, "
                          "(2) Learning AI without Training, or (3) Trained AI? ")
        try:
            game_type = int(game_type)
            if 1 <= game_type <= 3:
                break
            else:
                print('Please choose the game type number (1, 2, or 3)')
                continue
        except:
            print('Please choose the game type by number (1, 2, or 3)')
            continue
    return game_type


def max_stick_choice(game_sticks):
    '''
    Returns max number of sticks player can pick up
    '''
    max_stick_choice = 3
    if game_sticks < 3:
        max_stick_choice = game_sticks
    return max_stick_choice


def get_stick_choice(player, max_stick_choice, min_stick_choice=1):
    '''
    Gets player's choice of number of sticks to take
    '''
    player_move = ''
    while True:
        if max_stick_choice <= 3:
            player_move = input('{}: How many sticks do you take (1-3)? '.format(
                                player))
        else:
            player_move = input('How many sticks are there on the table initially '
                                '({}-{}) ?'.format(min_stick_choice, max_stick_choice))
        try:
            player_move = int(player_move)
            if min_stick_choice <= player_move <= max_stick_choice:
                break
            else:
                print('Please enter a number between {} and {}.'.format(
                      min_stick_choice, max_stick_choice))
                continue
        except:
            print('Please enter a number between {} and {}.'.format(
                  min_stick_choice, max_stick_choice))
            continue
    return player_move


def display_num_sticks(game_sticks):
    pass

def main():
    players = []

    pass


if __name__ == '__main__':
    main()
