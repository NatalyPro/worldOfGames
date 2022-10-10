import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    print(f"Random secret number {secret_number}")
    return secret_number


def get_guess_from_user(difficulty):
    try:
        player_number = int(input(f"Please select number from 1 to {difficulty}: "))
        if player_number > difficulty or player_number == 0:
            print("Critical error")
            raise ValueError("number does not exist")
        else:
            print(f"You selected {player_number}")
        return player_number
    except Exception as e:
        print(f"Exception {e}")


def compare_results(secret_number, player_number):
    if secret_number == player_number:
        return True
    else:
        return False


def play(difficulty):
    if difficulty == 1:
        if compare_results(generate_number(5), get_guess_from_user(5)):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if difficulty == 2:
        if compare_results(generate_number(10), get_guess_from_user(10)):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if difficulty == 3:
        if compare_results(generate_number(15), get_guess_from_user(15)):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if difficulty == 4:
        if compare_results(generate_number(20), get_guess_from_user(20)):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if difficulty == 5:
        if compare_results(generate_number(25), get_guess_from_user(25)):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

