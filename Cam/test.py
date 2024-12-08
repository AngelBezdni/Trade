import cv2

def cam():
    # Подключаемся к камере
    cap = cv2.VideoCapture(0)
    # Проверяем успешность подключения
    if not cap.isOpened():
        print("Не удалось открыть камеру.")
    else:
        # Делаем захват кадра
        ret, frame = cap.read()

        # Проверяем успешность захвата
        if ret:
            # Сохраняем кадр в файл
            cv2.imwrite('camera_capture.jpg', frame)
            print("Скрин был сохранён как camera_capture.jpg.")
        else:
            print("Не удалось захватить кадр.")
    # Освобождаем ресурсы
    cap.release()
    cv2.destroyAllWindows()


def video():
    # Открываем камеру
    cap = cv2.VideoCapture(0)

    # Устанавливаем разрешение записи
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Настройки кодека и файла вывода
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

    while cap.isOpened():
        # Захватываем кадр за кадром
        ret, frame = cap.read()

        if ret:
            # Записываем кадр в файл
            out.write(frame)

            # Показываем кадр на экране
            cv2.imshow('Video Recording', frame)

            # Завершаем запись по клавише 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Освобождаем реwсурсы
    cap.release()
    out.release()
    cv2.destroyAllWindows()

video()