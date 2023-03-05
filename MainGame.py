import CurrencyRouletteGame
import GuessGame
import MemoryGame
from Live import select_game, welcome, select_difficulty, check_if_player_wants_to_continue
from GameData import get_data

print(welcome(get_data("config.json", "name")))

game_continuation = True


def check_if_player__wants_to_continue():
    global game_continuation
    game_continuation = check_if_player_wants_to_continue()


if game_continuation:
    game_data = select_game()

    for x in game_data.keys():
        if game_data.keys().__contains__(2):
            difficulty = select_difficulty()
            GuessGame.play(difficulty)
        elif game_data.keys().__contains__(1):
            MemoryGame.play()
        elif game_data.keys().__contains__(3):
            CurrencyRouletteGame.play()
        else:
            print("ERROR ! Game does not exist")
    check_if_player__wants_to_continue()
else:
    print("Thank you for playing")
