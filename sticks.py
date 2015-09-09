import random


def get_game_mode():
    '''Asks user who they would like to play against and returns the corresponding
       number.
        [1] Another player
        [2] AI
        [3] Trained AI
    '''
    while True:
        game_mode = input("Select your desired game mode by number:\n  (1) Another Player,"
                          "\n  (2) Learning AI without Training, or \n  (3) Trained AI?\n> ")
        try:
            game_mode = int(game_mode)
            if 1 <= game_mode <= 3:
                break
            else:
                print('Please choose the game type number (1, 2, or 3)')
                continue
        except:
            print('Please choose the game type by number (1, 2, or 3)')
            continue
    return game_mode


def player_name(player_num):
    player = None
    while True:
        player = input("Please enter your name (or press Enter to be known "
                       "as 'Player {}')\n> ".format(player_num))
        if len(player) == 0:
            return 'Player {}'.format(player_num)
        elif len(player) < 25:
            for char in player:
                if not char.isalnum():
                    print('Player name must be letters and numbers only, and less than 25 characters')
                    continue
            return player
        else:
            print('Player name must be letters and numbers, and less than 25 characters')
            continue


# def max_stick_choice(game_sticks):
#     '''
#     Returns max number of sticks player can pick up
#     '''
#     max_stick_choice = 3
#     if game_sticks < 3:
#         max_stick_choice = game_sticks
#     return max_stick_choice


def get_stick_choice(player, min_stick_choice=1, max_stick_choice=3):
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
                                '({}-{})?\n> '.format(min_stick_choice, max_stick_choice))
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
    return 'There are {} sticks on the board.'.format(game_sticks)


def new_stick_total(game_sticks, player_stick_choice):
    return game_sticks - player_stick_choice


def is_game_over(game_sticks):
    if game_sticks <= 0:
        return True
    else:
        return False


def user_continue():
    user_continue = ''
    continue_bool = False
    while True:
        user_continue = input("Play again? [Y/n]: ").lower()
        if user_continue == '' or user_continue == 'y':
            continue_bool = True
            break
        elif user_continue == 'n':
            continue_bool = False
            print('\nGoodbye\n\n')
            break
        else:
            continue
    return continue_bool


def initialize_ai_dict():
    ret_dict = {}
    for n in list(range(1,101)):
        ret_dict[n] = {'hat': [1, 2, 3], 'beside': []}
    return ret_dict


def generate_ai_beside(ai_dict, game_sticks):
    return ai_dict[game_sticks]['beside'].append(random.randint(1,3))

def game_loop(player, game_sticks, game_mode):
    count = 0           # Enables tracking of whose turn it is
    play_again = False  # Signals whether player wants to continue playing

    while True:
        print(display_num_sticks(game_sticks))

        player_move = get_stick_choice(player[count % 2])

        game_sticks = new_stick_total(game_sticks, player_move)

        if is_game_over(game_sticks):
            print('\n{}, you lose.\n\n'.format(player[count % 2]))
            break
            # Potential spot to have return of win to AIs
        count += 1
    play_again = user_continue()

    return play_again


def main():
    players = []            # Holds player names and is the main structure for
                            # determining whose turn it is (in conjunction with count)
    min_start_sticks = 10
    max_start_sticks = 100
    game_sticks = 0         # Tracks number of sticks as game progresses
    game_mode = None        # 1: Player vs. Player, 2: Player vs. AI,
                            # 3: Player vs. Trained AI

    print('Welcome to the Game of Sticks!')

    while True:
        game_mode = get_game_mode()

        if game_mode == 1:
            players.append(player_name('1'))
            players.append(player_name('2'))
        elif game_mode == 2:
            players.append(player_name('1'))
            players.append('AI')
        else:
            players.append(player_name('1'))
            players.append('Trained AI')

        game_sticks = get_stick_choice(players[0], min_start_sticks, max_start_sticks)

        play_again = game_loop(players, game_sticks, game_mode)

        if not play_again:
            break


if __name__ == '__main__':
    main()
