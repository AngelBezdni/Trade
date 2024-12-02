from Def.script_def import *
import time


def main():
    # Вызов функции с заданными координатами
    #get_screen_text(x1=360, y1=233, x2=1867, y2=1035)

    orders = parse_json(process_screenshot("ORDER", 'screenshot.png'))

    print(f"Последний сигнал {orders[0]}") # Выводим первое значение

    minutes_passed = minutes_passed_since(orders[0]['date'], orders[0]['time'])

    print(f"Прошло времени с сигнала {minutes_passed} минут")

    TakeProfit = ""
    StopLoss = ""
    LimitPrice = ""
    Action = ""
    Quantity = ""

    if minutes_passed < 500:
        # Нажимае новый ордер


        # Take Profit
        TakeProfit = round(float(orders[0]['price']) + 0.07, 3)

        # Stop Loss
        StopLoss = round(float(orders[0]['price']) - 0.4, 3)

        # Limit Price
        LimitPrice = round(float(orders[0]['price']) - 0.02, 3)

        # Action
        Action = orders[0]['action']

        # Quantity
        Quantity = 0.05

    # Ждем перед следующим циклом
    time.sleep(10)

while True:
    main()



