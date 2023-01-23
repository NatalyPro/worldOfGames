#import MainScores
import GuessGame
import MemoryGame
from Live import select_game, welcome, select_difficulty
from GameData import get_data


print(welcome(get_data("config.json", "name")))
game_data = select_game()

for x in game_data.keys():
    if game_data.keys().__contains__(2):
        difficulty = select_difficulty()
        GuessGame.play(difficulty)
        #play(game_data.get(2))
        #MainScores.score_server()
    elif game_data.keys().__contains__(1):
        MemoryGame.play()
    else:
        print("ERROR ! Game is not created yet")
