#import MainScores
from Live import load_game, welcome
from GameData import get_data
from GuessGame import play

print(welcome(get_data("config.json", "name")))
game_data = load_game()

for x in game_data.keys():
    if game_data.keys().__contains__(2):
        play(game_data.get(2))
        #MainScores.score_server()
    else:
        print("ERROR ! Game is not created yet")
