import pyautogui
from mousDef import click_mouse
import os

file_path = r'D:\Основание\Progect Python\Skrin\Skrin\.venv\Script\new_order.png'

if os.path.exists(file_path):
    print("Путь к файлу верный.")
else:
    print("Путь к файлу неверен. Проверьте правильность написания.")


def find_new_chat_button(image_path):
    try:
        # Находим позицию кнопки "Новый чат" на экране
        button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)

        if button_location is not None:
            center_point = pyautogui.center(button_location)
            return center_point
        else:
            print(f"Кнопка не найдена. Изображение: {image_path}")
            return None
    except pyautogui.ImageNotFoundException:
        print(f"Кнопка не найдена. Изображение: {image_path}")
        return None

# Используем метод для поиска кнопки
button_coords = find_new_chat_button(file_path)
if button_coords:
    print(f"Координаты кнопки: {button_coords}")


if button_coords is not None:
    print(f"Координаты кнопки 'Новый чат': {button_coords}")
    click_mouse(button_coords.x, button_coords.y) # Нажимаем левую кнопку мыши



