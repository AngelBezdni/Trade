import pyautogui
import keyboard

def click_mouse(x, y): # перемещение и нажатие
    # Перемещаем курсор мыши к указанным координатам
    pyautogui.moveTo(x, y)

    # Нажимаем левую кнопку мыши
    pyautogui.click() # перемещение и нажати


def move_cursor_to(x, y):
    # Перемещение курсора к указанным координатам
    pyautogui.moveTo(x, y)# Перемещение курсора к указанным координатам


def right_click():
    # Нажатие правой кнопки мыши
    pyautogui.rightClick() # Нажатие правой кнопки мыши


def drag_and_drop(start_x, start_y, end_x, end_y):
    # Переходим к начальной точке
    pyautogui.moveTo(start_x, start_y)

    # Нажимаем левую кнопку мыши
    pyautogui.mouseDown()

    # Перетаскиваем мышь до конечной точки
    pyautogui.dragTo(end_x, end_y, duration=0.25)  # Параметр duration задает скорость перетаскивания

    # Отпускаем левую кнопку мыши
    pyautogui.mouseUp() # Перетаскиваем мышь до конечной точки


def keyNewOrder(x, y, text): # Нажимаем мышкой и вводим текст с клавиатуры

    pyautogui.moveTo(x, y) # Перемещаемся к координатам "Новый ордер"

    # Эмулируем клик левой кнопкой мыши
    pyautogui.click(button='left')

    # Вводим значение из переменной
    keyboard.write(str(text)) # Нажимаем мышкой и вводим текст с клавиатуры