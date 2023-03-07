def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play."


# def load_game_not_used():
# vgame_to_play = get_game_to_play()

# if game_to_play.isnumeric():
#    selected_game_to_play = int(game_to_play)
#   assert selected_game_to_play in range(1, 3)
# else:
#    raise ValueError("Game number not valid")

# difficulty_input = get_game_difficulty(1, 6)

# if difficulty_input.isnumeric():
#   selected_difficulty_input = int(difficulty_input)
#   assert selected_difficulty_input in range(1, 6)
# else:
#   raise ValueError("Game difficulty not valid")

# data = dict({selected_game_to_play: selected_difficulty_input})
# return data


def select_game():
    global game

    selected_game = get_game_to_play()
    if get_value_selected_2(selected_game, 1, 4, 'game'):
        game = get_value_selected_2(selected_game, 1, 4, 'game')
    else:
        exit()

    # selected_difficulty = get_game_difficulty(1, 6)
    # if get_value_selected_2(selected_difficulty, 'difficulty'):
    # difficulty = get_value_selected_2(selected_game, 'difficulty')
    # else:
    # exit()

    data = dict({game: game})
    return data


def option_to_continue_request():
    return input("Would you like to continue playing: \n"
                 "1 for yes \n"
                 "2 for no \n")


def check_if_player_wants_to_continue_not_used():
    value_selected = 0
    while value_selected < 3:
        selected_option = option_to_continue_request()
        if get_value_selected_2(selected_option, 1, 2, 'players response'):
            if get_value_selected_2(selected_option, 1, 2, 'players response') == 2:
                value_selected = False
            else:
                value_selected = True
        else:
            print("ERROR ! Wrong value selected . Try again")
    if value_selected == 3:
        print("Too many attempts. Exiting program.")
        return False


def check_if_player_wants_to_continue():
    global x
    for x in range(3):
        selected_option = option_to_continue_request()
        if get_value_selected_2(selected_option, 1, 3, 'players response'):
            if get_value_selected_2(selected_option, 1, 3, 'players response') == 2:
                return False
            else:
                return True
        else:
            print("ERROR ! Wrong value selected . Try again")
    if x == 3:
        print("Too many attempts. Exiting program.")
        return False


def select_difficulty():
    global difficulty
    selected_difficulty = get_game_difficulty()
    if get_value_selected_2(selected_difficulty, 1, 6, 'difficulty'):
        difficulty = get_value_selected_2(selected_difficulty, 1, 6, 'difficulty')
    else:
        exit()

    return difficulty


def get_value_selected(received_value, start_range, end_range, value_name):
    if received_value.isnumeric():
        value_to_return = int(received_value)
        assert value_to_return in range(start_range, end_range)
    else:
        raise ValueError(f"{value_name} number not valid")
    return value_to_return


def get_value_selected_2(received_value, start_range, end_range, value_name):
    if received_value.isnumeric():
        value_to_return = int(received_value)
        if value_to_return in range(start_range, end_range):
            return value_to_return
        else:
            print(f"{value_name} number not valid")
            return False
    else:
        print(f"{value_name} number not numeric")
        return False


def get_game_to_play():
    return input("Please choose a game to play: \n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                 "back: \n"
                 "2. Guess Game - guess a number and see if you chose like the computer \n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"
                 "Game to play: ")


def get_game_difficulty():
    return input(f"Please choose game difficulty from 1 to 5: ")


def check_game_difficulty(game_difficulty, start, end):
    if game_difficulty not in range(start, end):
        raise ValueError("Game difficulty not found")
    else:
        print(f"Game difficulty that was selected: {game_difficulty} \n Setting game difficulty...")


def check_game_to_play(game, start, end):
    if game not in range(start, end):
        raise ValueError("Game number not found")
    else:
        print(f"Game that was selected: {game} \n Starting the game...")
