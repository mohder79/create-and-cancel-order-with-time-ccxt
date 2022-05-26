import ccxt
from pprint import pprint
import api_confing_my_bybit as ac
import time


exchange = ccxt.bybit({
    'options': {
        'adjustForTimeDifference': True,
    },
    'apiKey': ac.API_KEY,
    'secret': ac.SECRET_KEY,
    'password': ac.PASSWORD,
})


markets = exchange.load_markets()
print(exchange)


symbol = 'BTC/USDT:USDT'
amount = 0.001
price = 25000
type = 'limit'
sl_tk = {
    'stop_loss': 24000,  # stop price
    'type': 'stopMarket',
    'take_profit': 33000,  # profit price
}


run = True
sleep_time = 40

while run == True:
    seconds = 0
    pprint('bot is working')

    order = exchange.create_limit_buy_order(
        symbol, amount, price, params=sl_tk)
    pprint(order)
    time.sleep(1)
    pprint('bot made your order ')
    time.sleep(1)
    while seconds != 5:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
    time.sleep(1)
    cancel_order = exchange.cancel_all_orders(symbol)
    pprint(cancel_order)
    time.sleep(1)
    pprint('bot cancel your order ')
    time.sleep(sleep_time)
