import tkinter as tk
from threading import Thread, Event
import time
from Main import Start


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ввод значения")
        self.geometry("300x100")

        # Поле для ввода значения
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        # Кнопка "Старт"
        self.start_button = tk.Button(self, text="Старт", command=self.start_loop)
        self.start_button.pack()

        # Кнопка "Стоп"
        self.stop_button = tk.Button(self, text="Стоп", command=self.stop_loop)
        self.stop_button.pack()

        # Флаг для остановки цикла
        self.stop_event = Event()

    def start_loop(self):
        if not self.stop_event.is_set():
            self.stop_event.clear()
            thread = Thread(target=self.loop)
            thread.start()

    def stop_loop(self):
        self.stop_event.set()

    def loop(self):
        while not self.stop_event.is_set():
            value = self.entry.get()  # Получаем значение из поля ввода
            print(f"Передано значение: {value}")

            # Здесь вызываем функцию Start(value)
            # Например:
            try:
                while True:
                    if self.stop_event.is_set():  # Проверяем флаг остановки внутри внутреннего цикла
                        break
                    Start(int(value))
                    time.sleep(0.01)  # Небольшая задержка для предотвращения зависания UI
            except ValueError:
                pass  # Обрабатываем возможные ошибки преобразования строки в число

            time.sleep(1)  # Задержка между итерациями

    def bind_escape(self, event):
        self.stop_event.set()
        self.destroy()


# Создаем экземпляр класса Application
app = Application()

# Привязываем событие нажатия клавиши Esc
app.bind("<Escape>", app.bind_escape)

# Запускаем основной цикл событий Tkinter
app.mainloop()