import random
import time

from GuessGame import get_guess_from_user_2


def generate_sequence(difficulty, from_number, to_number):
    generated_list = []
    for i in range(difficulty):
        random_num = random.choice(list_of_generated_numbers(from_number, to_number))
        generated_list.append(random_num)
    return generated_list


def check_value_is_correct(value, to_amount, from_amount, value_name):
    if value.isnumeric():
        value_int = int(value)

        if value_int == 0 or value_int > to_amount or value_int < from_amount:
            print(f"Invalid {value_name} selected")
            exit()
        else:
            correct_value = value_int
            print()
            return correct_value
    else:
        print(f"{value_name} not numeric")
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
    selected_difficulty = select_difficulty(5, 10)
    checked_difficulty = check_value_is_correct(selected_difficulty, 10, 5, 'difficulty')
    generated_list = generate_sequence(checked_difficulty, 1, 101)
    show_generated_list_to_player(generated_list)
    if is_list_equal(generated_list, get_list_from_user(selected_difficulty)):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def select_difficulty(diff_from, diff_to):
    difficulty = input(f"Please choose difficulty from {diff_from} to {diff_to}: \n")
    return difficulty


def show_generated_list_to_player(generated_list):
    print("generated list " + str(generated_list))
    time.sleep(7)
    print("ending to show generated list to player")
