from Def.script_def import *
from Def.mousDef import *
import time
from pynput.keyboard import Key, Controller
from datetime import datetime as dt
import pyperclip

def Start(interval):
    current_time = datetime.now()
    if current_time.second == 1 and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        valu()
    elif current_time.second == 5 and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        valu()
    elif current_time.second == 10 and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        valu()
    time.sleep(1)

def click_click(text):
    # M30
    click_mouse(220, 126)
    main(text)
    # H1
    click_mouse(254, 125)
    main(text)
    #H2
    click_mouse(282, 125)
    main(text)
    #H3
    click_mouse(308, 125)
    main(text)

def valu():
    # AUDJPY
    click_mouse(1573, 315)
    click_click('AUDJPY')

    #USDCHF
    click_mouse(1575, 348)
    click_click('USDCHF')

    #EURJPY
    click_mouse(1579, 374)
    click_click('EURJPY')


def main(text):
    # Вызов функции с заданными координатами
    try:
        tiker = text
        click_mouse(341, 875)
        time.sleep(5)
        get_screen_text(63, 899, 1509, 1033, 'screenshot.png')

        orders = process_screenshot_vxod("ORDER", 'screenshot.png')

        print(orders) # Выводим строку

        # Разделение строки на части по пробелу
        parts = orders.split()

        # Извлечение даты и времени
        date_time = parts[-4] + ' ' + parts[-3]

        Action = parts[-5]

        # Вывод результата
        print(date_time)
        print(Action)

        minutes_passed = minutes_passed_since(parts[-4], parts[-3] + ":00")

        print(f"Прошло времени с сигнала {minutes_passed} минут")

        TakeProfit = ""
        StopLoss = ""
        LimitPrice = ""
        Quantity = ""


        if minutes_passed < 15:

            # Закрываем браузер
            #click_mouse(1899, 17)

            # Сворачиваем браузер
            click_mouse(1804, 16)

            # Нажимае новый ордер
            click_mouse(319, 57)
            time.sleep(1)
            click_mouse(958, 229)

            if tiker == "AUDJPY":
                click_mouse(1002, 247)
            elif tiker == "USDCHF":
                click_mouse(839, 262)
            elif tiker == "EURJPY":
                click_mouse(824, 273)

            time.sleep(5)
            get_screen_text(778, 384, 916, 414, 'Last.png')
            Last = process_screenshot_TEXT("ORDER", 'Last.png')
            print(Last)

            zap = 3
            # Take Profit
            Mnoj = 0.07
            if tiker == "USDCHF":
                Mnoj = 0.0007
                zap = 5
            if Action == "buy" or Action == "Buy":
                TakeProfit = round(float(Last) + Mnoj, zap)
            elif Action == "sell" or Action == "Sell" or Action == "Sell.":
                TakeProfit = round(float(Last) - Mnoj, zap)
            keyNewOrder(1046, 283, TakeProfit)
            time.sleep(3)

            # Stop Loss
            Mnoj = 0.4
            if tiker == "USDCHF":
                Mnoj = 0.004
                zap = 5
            if Action == "buy" or Action == "Buy":
                StopLoss = round(float(Last) - Mnoj, zap)
            elif Action == "sell" or Action == "Sell" or Action == "Sell.":
                StopLoss = round(float(Last) + Mnoj, zap)

            keyNewOrder(832,283,StopLoss)
            time.sleep(3)

            # Limit Price
            LimitPrice = round(float(Last) - 0.02, 3)

            # Quantity
            Quantity = 0.01
            keyNewOrder(853, 257, Quantity)
            time.sleep(3)

            #print("Ждем 5000")
            #time.sleep(5000)
            if Action == "buy" or Action == "Buy":
                click_mouse(1030, 447)
                time.sleep(3)
            elif Action == "sell" or Action == "Sell" or Action == "Sell.":
                click_mouse(824, 445)
                time.sleep(3)

            click_mouse(1125, 191)

            click_mouse(509, 1060)

            # Ждем перед следующим циклом


            time.sleep(10)
        else:
            print("Сигнал не найдет")

    except Exception as e:
        print("Произошла ошибка:", e)



while True:
    Start(1)






