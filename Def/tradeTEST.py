import re
import pyautogui
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import time

from Main import timeSleep


def get_screen_text(x1, y1, x2, y2, Name):
    # Делаем скриншот указанной области экрана
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

    # Сохраняем скриншот в файл, чтобы tesseract мог его обработать
    screenshot.save(Name)

def process_screenshot_last(image):
    # Открываем изображение
    img = Image.open(image)

    # Используем Tesseract OCR для получения текста с изображения
    text = pytesseract.image_to_string(img)

    return text

time.sleep(3)
get_screen_text(729, 988, 840, 1029, 'screenshot.png')

last30 = process_screenshot_TEXT('screenshot.png').split()[0]

print(last30)