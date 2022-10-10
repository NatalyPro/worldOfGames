def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play."


def load_game():
    try:
        game_to_play = get_game_to_play()
        difficulty_input = get_game_difficulty()
        data = dict({game_to_play: difficulty_input})
        try:
            check_game_to_play(game_to_play, 1, 4)
        except ValueError as e:
            if len(e.args) > 0:
                print("Game number not found")
                quit()
            else:
                print(e.args)

        try:
            check_game_difficulty(difficulty_input, 1, 6)
        except ValueError as e:
            if len(e.args) > 0:
                print("Game difficulty not found")
                quit()
            else:
                print(e.args)
        return data
    except Exception as e:
        print("something went wrong")
        print(e.args)


def get_game_to_play():
    return int(input("Please choose a game to play: \n"
                     "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                     "back: \n"
                     "2. Guess Game - guess a number and see if you chose like the computer \n"
                     "3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"
                     "Game to play: "))


def get_game_difficulty():
    return int(input("Please choose game difficulty from 1 to 5: "))


def check_game_difficulty(game_difficulty, start, end):
    if game_difficulty not in range(start, end):
        raise ValueError('Game difficulty not found')
    else:
        print(f"Game difficulty that was selected: {game_difficulty} \n Setting game difficulty...")


def check_game_to_play(game_to_play, start, end):
    if game_to_play not in range(start, end):
        raise ValueError("Game number not found")
    else:
        print(f"Game that was selected: {game_to_play} \n Starting the game...")
