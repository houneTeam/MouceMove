import pyautogui
import time

# Координаты для перемещения
coordinates = [(655, 623), (254, 778)]

try:
    while True:
        for x, y in coordinates:
            pyautogui.moveTo(x, y, duration=0.5)  # Перемещение курсора к указанным координатам за 0.5 секунды
            time.sleep(1)  # Задержка 1 секунда перед следующим перемещением
except KeyboardInterrupt:
    print("Программа остановлена пользователем.")
