import json


def save_data(names_file, data, save_mode):
    my_file = open(names_file, save_mode)
    my_file.write(str(data))
    my_file.close()


def get_data(names_file, key_input):
    my_file = open(names_file, "r")
    data = json.loads(my_file.read())
    for d in data['data']:
        # print(d, end='')
        for key in d:
            if key == key_input:
                # (f"{d[key]} \n")
                return d[key]
    my_file.close()


# save_data("config.json")
get_data("config.json", "name")
