import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
from .mousDef import click_mouse
import tkinter as tk
import pyautogui
import re
import json
from datetime import datetime, timezone


def preprocess_image(image): # Преобразование в оттенки серого
    # Преобразование в оттенки серого
    gray_image = image.convert('L')

    # Увеличение контраста
    enhancer = ImageEnhance.Contrast(gray_image)
    contrasted_image = enhancer.enhance(2.0)

    # Применение фильтра для повышения резкости
    sharp_image = contrasted_image.filter(ImageFilter.SHARPEN)

    return sharp_image

def get_screen_text(x1, y1, x2, y2):
    # Делаем скриншот указанной области экрана
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

    # Сохраняем скриншот в файл, чтобы tesseract мог его обработать
    screenshot.save('screenshot.png')

def process_screenshot(search, image): # Преобразуем список словарей в JSON
    # Открываем изображение
    img = Image.open(image)

    # Используем Tesseract OCR для получения текста с изображения
    text = pytesseract.image_to_string(img)

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

    # Количество полных минут, прошедших с заданного времени
    minutes_passed = int(delta.total_seconds() / 60)

    return minutes_passed