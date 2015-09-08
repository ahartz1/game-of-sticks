import random


def max_stick_choice(game_sticks):
    '''
    Returns max number of sticks player can pick up
    '''
    max_stick_choice = 3
    if game_sticks < 3:
        max_stick_choice = game_sticks
    return max_stick_choice


def get_player_move(player, max_stick_choice, min_stick_choice=1):
    '''
    Gets player's choice of number of sticks to take
    '''
    player_move = ''
    while True:
        player_move = input('{}: How many sticks do you take ({}-{})? $> '.format(
                            player, min_stick_choice, max_stick_choice))
        try:
            player_move = int(player_move)
            if player_move <= max_stick_choice and player_move >= min_stick_choice:
                break
            else:
                continue
        except:
            continue
        return player_move


def main():
    pass


if __name__ == '__main__':
    main()
