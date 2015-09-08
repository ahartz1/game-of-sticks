import random


def max_stick_choice(game_sticks):
    '''
    Returns max number of sticks player can pick up
    '''
    max_stick_choice = 3
    if game_sticks < 3:
        max_stick_choice = game_sticks
    return max_stick_choice


def get_player_move(max_stick_choice, player):
    '''
    Gets player's choice of number of sticks to take
    '''
    #TODO prompt user to enter input
    print('{} sticks are available. {}, how many sticks will you take?'.format(
          max_stick_choice, player))


def ask_player_input(max_stick_choice):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
