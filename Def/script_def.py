import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
from .mousDef import click_mouse
import tkinter as tk
import pyautogui
import re
import json
import webbrowser
import schedule
import time
from datetime import datetime, timedelta, timezone



def preprocess_image(image): # Преобразование в оттенки серого
    # Преобразование в оттенки серого
    gray_image = image.convert('L')

    # Увеличение контраста
    enhancer = ImageEnhance.Contrast(gray_image)
    contrasted_image = enhancer.enhance(2.0)

    # Применение фильтра для повышения резкости
    sharp_image = contrasted_image.filter(ImageFilter.SHARPEN)

    return sharp_image

def get_screen_text(x1, y1, x2, y2, Name):
    # Делаем скриншот указанной области экрана
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

    # Сохраняем скриншот в файл, чтобы tesseract мог его обработать
    screenshot.save(Name)

def process_screenshot(search, image): # Преобразуем список словарей в JSON
    # Открываем изображение
    img = Image.open(image)

    # Используем Tesseract OCR для получения текста с изображения
    text = pytesseract.image_to_string(img)
    print(text)

    # Разбиваем текст на строки
    lines = text.split('\n')

    # Создаем пустой список для хранения пар ключ-значение
    data_list = []

    # Проходимся по каждой строке и разбираем её на ключ и значение
    for line in lines:
        # Убираем лишние пробелы и проверяем наличие 'search'
        line = line.strip()

        if search in line:
            # Удаляем всё, что идет до 'search'
            index_search = line.find(search)
            line = line[index_search:]

            # Находим позицию первого символа ':'
            colon_index = line.find(':')

            if colon_index != -1:
                # Делим строку на ключ и значение
                key = line[:colon_index].strip()
                value = line[colon_index + 1:].strip()

                # Добавляем пару ключ-значение в виде словаря в список
                data_list.append({key: value})

    # Преобразуем список словарей в JSON
    json_data = json.dumps(data_list, indent=4, ensure_ascii=False).encode('utf8').decode()

    return json_data

def parse_order_string(order_str):
    # Регулярное выражение для поиска пар 'ключ: значение'
    pattern = r'(\w+):\s*([^,]+)'
    
    # Находим все пары 'ключ: значение' в строке
    matches = re.findall(pattern, order_str)
    
    # Преобразуем найденные пары в словарь
    result = {}
    for match in matches:
        if match[0] == 'timenow':
            date_time = match[1].split('T')
            result['date'] = date_time[0]
            result['time'] = date_time[1]
        else:
            result[match[0]] = match[1]
            
    return result

def parse_json(input_json):# Парсим JSON
    # Парсим JSON
    data = json.loads(input_json)

    # Создаем пустой список для хранения всех сущностей
    all_orders = []

    # Проходимся по каждому объекту в списке
    for order_obj in data:
        # Извлекаем строку ORDER
        order_str = order_obj['ORDER']
        
        # Преобразуем строку ORDER в словарь
        order_dict = parse_order_string(order_str)
        
        # Добавляем словарь в общий список
        all_orders.append(order_dict)

    return all_orders

def convert_to_8_chars_and_z(time_str):
    # Оставляем только первые 8 символов и добавляем "Z"
    converted_time = time_str[:8] + "Z"
    return converted_time

def minutes_passed_since(date, time):
# Заданная дата и время

    time = convert_to_8_chars_and_z(time)

    # Конкатенируем дату и время для создания полной временной метки
    given_datetime_str = f'{date}T{time}'

    # Преобразуем строку в объект datetime
    given_datetime = datetime.strptime(given_datetime_str, '%Y-%m-%dT%H:%M:%S%z')

    # Текущее время
    current_datetime = datetime.now().astimezone()

    # Вычисляем разницу во времени
    delta = current_datetime - given_datetime


    # print(f"{current_datetime} -  {given_datetime} = {delta}")

    # Количество полных минут, прошедших с заданного времени
    minutes_passed = int(delta.total_seconds() / 60)

    return minutes_passed + 180

def open_tradingview_page():
    url = "https://ru.tradingview.com/chart/R07wFehy/"
    webbrowser.open(url)

def reset_and_start_scheduler():
    # Сбрасываем текущий планировщик
    schedule.clear()

    # Получаем текущее время
    now = datetime.now()

    # Определяем ближайшее время для выполнения задачи
    next_run_time = now.replace(second=1, microsecond=0)
    print(next_run_time)
    if now.minute >= 30:
        next_run_time += timedelta(minutes=60 - now.minute)
    else:
        next_run_time += timedelta(minutes=30 - now.minute)
    print(next_run_time)
    # Ждем до следующего подходящего времени
    time_to_wait = (next_run_time - now).total_seconds()
    time.sleep(time_to_wait)

    # Выполняем задачу в первый раз
    main()

    # Устанавливаем регулярное расписание
    schedule.every(30).minutes.do(main)

    # Запускаем задачу каждую 5 минут
    #schedule.every(5).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)


def process_screenshot_vxod(search, image):
    # Открываем изображение
    img = Image.open(image)

    # Используем Tesseract OCR для получения текста с изображения
    text = pytesseract.image_to_string(img)

    # Разбиваем текст на строки
    lines = text.split('\n')
    #print(text)
    result = None

    # Проходимся по каждой строке и ищем строку, начинающуюся с 'Bxog'
    for line in lines:
        # Убираем лишние пробелы
        line = line.strip()

        if line.startswith("Bxog"):
            result = line
        elif line.startswith("Bxoa"):
            result = line
            break

    return result

def process_screenshot_TEXT(search, image):
    # Открываем изображение
    img = Image.open(image)

    # Используем Tesseract OCR для получения текста с изображения
    text = pytesseract.image_to_string(img)

    return text



