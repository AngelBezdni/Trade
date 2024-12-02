import schedule
import time
from datetime import datetime, timedelta




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

    while True:
        schedule.run_pending()
        time.sleep(1)


# Запускаем планировщик
reset_and_start_scheduler()