import time
from os import system, name

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 400


def screen_cleaner():
    time.sleep(7)
    clear()


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


