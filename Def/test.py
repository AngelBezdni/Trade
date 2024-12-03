from Def.script_def import *
from Def.mousDef import *
import time
from pynput.keyboard import Key, Controller
from datetime import datetime as dt
import pyperclip

keyboard = Controller()  # Переменная для управления клавиатурой


def start(interval):
    current_time = datetime.now()

    # Проверка выполнения условия каждые 1, 5 и 10 секунд при совпадении минуты с интервалом
    if current_time.second in [1, 5, 10] and current_time.minute % interval == 0:
        print(f"Current_time: {current_time} \n заданный интервал: {interval}")
        valu()


def click_click(ticker):
    # Общие клики для всех тикеров
    for x, y in [(220, 126), (254, 125), (282, 125), (308, 125)]:
        click_mouse(x, y)
        main(ticker)


def valu():
    # Работа с каждым тикером
    tickers = [
        ("AUDJPY", 1573, 315),
        ("USDCHF", 1575, 348),
        ("EURJPY", 1579, 374)
    ]

    for ticker, x, y in tickers:
        click_mouse(x, y)
        click_click(ticker)


def main(ticker):
    try:
        # Вызов функции с заданными координатами
        click_mouse(341, 875)
        time.sleep(5)

        # Получение скриншота и обработка данных
        get_screen_text(63, 899, 1509, 1033, 'screenshot.png')
        orders = process_screenshot_vxod("ORDER", 'screenshot.png')
        parts = orders.split()

        # Извлечение даты и времени
        date_time = parts[-4] + ' ' + parts[-3]
        action = parts[-5]

        # Вывод результата
        # print(date_time)
        # print(action)

        minutes_passed = minutes_passed_since(parts[-4], parts[-3] + ":00")
        # print(f"Прошло времени с сигнала {minutes_passed} минут")

        take_profit = ""
        stop_loss = ""
        limit_price = ""
        quantity = ""

        if minutes_passed < 15:
            # Сворачивание браузера
            click_mouse(1804, 16)

            # Открытие нового ордера
            click_mouse(319, 57)
            time.sleep(1)
            click_mouse(958, 229)

            # Выбор тикера
            if ticker == "AUDJPY":
                click_mouse(1002, 247)
            elif ticker == "USDCHF":
                click_mouse(839, 262)
            elif ticker == "EURJPY":
                click_mouse(824, 273)

            time.sleep(5)
            get_screen_text(778, 384, 916, 414, 'Last.png')
            last = process_screenshot_TEXT("ORDER", 'Last.png')
            print(last)

            # Установка значений
            mnoj = 0.07
            zap = 3
            if ticker == "USDCHF":
                mnoj = 0.0007
                zap = 5

            # Take Profit
            take_profit = round(float(last) + mnoj, zap)
            key_new_order(1046, 283, take_profit)
            time.sleep(3)

            # Stop Loss
            stop_loss = round(float(last) - mnoj * 8, zap)
            key_new_order(832, 283, stop_loss)
            time.sleep(3)

            # Limit Price
            limit_price = round(float(last) - 0.02, 3)

            # Quantity
            quantity = 0.01
            key_new_order(853, 257, quantity)
            time.sleep(3)

            # Выполнение сделки
            if action.lower() == "buy":
                click_mouse(1030, 447)
                time.sleep(3)
            elif action.lower() == "sell":
                click_mouse(824, 445)
                time.sleep(3)

            click_mouse(1125, 191)
            click_mouse(509, 1060)

            # Пауза перед следующим циклом
            time.sleep(10)
        else:
            print("Сигнал не найден")

    except Exception as e:
        print("Произошла ошибка:", e)

while True:
    start(1)
