from Def.script_def import *
from Def.mousDef import *
import time
from pynput.keyboard import Key, Controller
from datetime import datetime as dt


def Start(interval = 5):
    current_time = datetime.now()
    if current_time.second == 1 and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        main()
    elif current_time.second == 5 and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        main()
    elif current_time.second == 10 and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        main()
    time.sleep(1)



def main():
    # Вызов функции с заданными координатами
    try:
        open_tradingview_page()
        time.sleep(10)
        get_screen_text(x1=360, y1=233, x2=1867, y2=1035)

        orders = parse_json(process_screenshot("ORDER", 'screenshot.png'))

        print(f"Последний сигнал {orders[0]}") # Выводим первое значение

        minutes_passed = minutes_passed_since(orders[0]['date'], orders[0]['time'])

        print(f"Прошло времени с сигнала {minutes_passed} минут")

        TakeProfit = ""
        StopLoss = ""
        LimitPrice = ""
        Action = ""
        Quantity = ""
        keyboard = Controller()

        if minutes_passed < 1 and orders[0]['size'] != 0:
            print(orders[0]['size'])
            # Закрываем браузер
            click_mouse(1899, 17)

            # Нажимае новый ордер
            click_mouse(319, 57)

            # Take Profit
            TakeProfit = round(float(orders[0]['price']) + 0.07, 3)
            keyNewOrder(1072, 281, TakeProfit)

            # Stop Loss
            StopLoss = round(float(orders[0]['price']) - 0.4, 3)
            keyNewOrder(862,280,StopLoss)

            # Limit Price
            LimitPrice = round(float(orders[0]['price']) - 0.02, 3)

            # Action
            Action = orders[0]['action']

            # Quantity
            Quantity = 0.01
            keyNewOrder(853, 257, Quantity)

            if Action == "buy":
                click_mouse(1030, 447)
            elif Action == "sell":
                click_mouse(824, 445)

            click_mouse(1125, 191)

            # Ждем перед следующим циклом


            time.sleep(10)
            open_tradingview_page()
            time.sleep(10)
        else:
            click_mouse(1899, 17)

    except Exception as e:
        print("Произошла ошибка:", e)



while True:
    Start()


