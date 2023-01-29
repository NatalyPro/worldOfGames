import requests
import json
from datetime import date, datetime, timedelta
from MemoryGame import select_difficulty, check_value_is_correct, is_list_equal
from GuessGame import generate_number


def get_currency_exchange_rate(currency_from, currency_to, start_date, end_date):
    request_url = f'https://fxds-public-exchange-rates-api.oanda.com/cc-api/currencies?base={currency_from}&quote={currency_to}&data_type=general_currency_pair&start_date={start_date}&end_date={end_date}'
    print(f"access api to get current exchange rate : {request_url}")
    response = requests.get(request_url)  # get full response

    response_dict = json.loads(response.text)
    print(type(response_dict))  # dict

    for r in response_dict["response"]:
        print(r["average_bid"])
        value = r["average_bid"]

        return value

    # new_response = [{"currency": repo["average_bid"]} for repo in response_dict.json()]
    # print(new_response)
    # response_dict = json.loads(response.text)
    # print(f"get response in json : {response_dict}")
    # for i in response_dict:
    #     print("key: ", i, "val: ", response_dict[i])
    #     new_response = response_dict[i]

    # new_response = [{"currency": repo["average_bid"]} for repo in response.json()]

    # for repo in new_response:
    #    print(repo)


def get_yesterday_date():
    yesterday_date = datetime.now() - timedelta(days=1)
    edited_yesterday_date = yesterday_date.strftime('%Y-%m-%d')
    return edited_yesterday_date


def play():
    selected_difficulty = check_value_is_correct(select_difficulty(1, 6), 6, 1, 'difficulty')
    show_generated_number_to_player = generate_number(101)
    number_from_player = check_value_is_correct(get_guess_number_from_player(show_generated_number_to_player), 99999999,
                                                1, 'exchange rate')
    current_exchange_rate = get_currency_exchange_rate('USD', 'ILS', get_yesterday_date(), date.today())
    get_money_interval(current_exchange_rate, selected_difficulty)
    # is_list_equal replace with math.isclose()
    if is_list_equal(number_from_player, get_money_interval(current_exchange_rate, selected_difficulty)):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def get_guess_number_from_player(generated_number):
    generated_number_from_user = input(f"Guess current exchange rate from USD to ILS for amount {generated_number}: \n")
    return generated_number_from_user


def get_money_interval(currency_rate, difficulty):
    currency_rate_float = float(currency_rate)
    money_interval = (currency_rate_float - (5 - difficulty), currency_rate_float + (5 - difficulty))
    print(money_interval)
    return money_interval
