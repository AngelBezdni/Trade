import cv2

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