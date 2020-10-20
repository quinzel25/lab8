import requests 
from pprint import pprint 



def main():

    num_of_bits = get_user_input()
    call = requests_bitcoin()
    exchange_rate = get_bitcoin_exchange_rate(call)
    value = convert_bitcoin(num_of_bits, exchange_rate)
    print(f'{num_of_bits} Bitcoin is equivalent to ${value}')


def get_user_input():

    bitcoin = float(input('Enter the number of bitcoin: '))

    return bitcoin


def requests_bitcoin():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    return data
def get_bitcoin_exchange_rate(data):
    
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    return dollars_exchange_rate

def convert_bitcoin(user_input, exchange_rate):

    value = user_input * exchange_rate
    return value

if __name__ == "__main__":
    main()

