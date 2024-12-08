import ctypes


# Получение хэндла окна
hwnd = ctypes.windll.user32.GetForegroundWindow()

# Функция для перемещения курсора
def move_cursor(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

# Функция для нажатия левой кнопки мыши
def left_click():
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)  # Нажатие левой кнопки
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)  # Отпускание левой кнопки

def mouseClickAPI(x, y):
    # Переместить курсор в точку (100, 200)
    move_cursor(x, y)
    # Нажать левую кнопку мыши
    left_click()