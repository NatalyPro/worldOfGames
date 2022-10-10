from GameData import save_data
from Utils import SCORES_FILE_NAME


def get_score():
    my_file = open(SCORES_FILE_NAME, "r")
    score = my_file.read()
    print(f"Score found {score}")
    return score


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    print(f"points of winning {points_of_winning}")
    score = 0
    if len(get_score()) != 0:
        calculated_score = int(get_score()) + points_of_winning
    else:
        calculated_score = int(score) + points_of_winning
    save_data(SCORES_FILE_NAME, calculated_score, "w")
