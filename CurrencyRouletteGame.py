import requests
import json
from datetime import date, datetime, timedelta


def get_currency_exchange_rate(currency_from, currency_to, start_date, end_date):
    request_url = f'https://fxds-public-exchange-rates-api.oanda.com/cc-api/currencies?base={currency_from}&quote={currency_to}&data_type=general_currency_pair&start_date={start_date}&end_date={end_date}'
    print(f"access api to get current exchange rate : {request_url}")
    response = requests.get(request_url)  # get full response

    response_dict = json.loads(response.text)
    print(type(response_dict))  #dict

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


# full
# for repo in response.json():
#     if "first" in repo["full_name"]:
#         result.append(repo["full_name"])

get_currency_exchange_rate('USD', 'ILS', get_yesterday_date(), date.today())


def get_money_interval(currency_rate, difficulty, random_number):
    print()
