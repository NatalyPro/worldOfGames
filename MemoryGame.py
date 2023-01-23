import random
import this
import time

from GuessGame import get_guess_from_user_2


def generate_sequence(difficulty, from_number, to_number):
    generated_list = []
    for i in range(difficulty):
        random_num = random.choice(list_of_generated_numbers(from_number, to_number))
        generated_list.append(random_num)
    return generated_list


def check_difficulty_is_correct(difficulty, to_difficulty, from_difficulty):
    if difficulty.isnumeric():
        difficulty_int = int(difficulty)

        if difficulty_int == 0 or difficulty_int > to_difficulty or difficulty_int < from_difficulty:
            print("Invalid difficulty selected")
            exit()
        else:
            correct_difficulty = difficulty_int
            print()
            return correct_difficulty
    else:
        print("difficulty not numeric")
        exit()


def list_of_generated_numbers(from_number, to_number):
    list_of_numbers = []
    for i in range(from_number, to_number):
        list_of_numbers.append(i)
    return list_of_numbers


def get_list_from_user(difficulty):
    player_list = []
    if difficulty.isnumeric():
        difficulty_int = int(difficulty)
        for i in range(difficulty_int):
            number = get_guess_from_user_2(101)
            player_list.append(number)
    else:
        print("difficulty not numeric")
        exit()
    return player_list


def is_list_equal(generated_list, player_list):
    if generated_list == player_list:
        return True
    else:
        return False


def play():
    selected_difficulty = select_difficulty()
    checked_difficulty = check_difficulty_is_correct(selected_difficulty, 10, 5)
    generated_list = generate_sequence(checked_difficulty, 1, 101)
    show_generated_list_to_player(generated_list)
    if is_list_equal(generated_list, get_list_from_user(selected_difficulty)):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def select_difficulty():
    difficulty = input("Please choose difficulty from 5 to 10: \n")
    return difficulty


def show_generated_list_to_player(generated_list):
    print("generated list " + str(generated_list))
    time.sleep(0.7)
    print("ending to show generated list to player")
