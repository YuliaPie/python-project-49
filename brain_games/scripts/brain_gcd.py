#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times

name = main()
print('Find the greatest common divisor of given numbers.')
def gcd_randoms():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    question = f"{first} {second}"
    randoms = [first, second]
    randoms.sort()
    first = randoms[0]
    second = randoms[1]
    n = first
    while True:
        if second % n == 0 and first % n == 0:
            return [question, n]
        else:
            n -= 1

gcd_randoms = [gcd_randoms(),gcd_randoms(),gcd_randoms()]
ask_three_times(gcd_randoms, name)
"""

Задачи

Добавьте еще одну запись в секцию [tool.poetry.scripts] в pyproject.toml
Проверьте работоспособность новой игры
Добавьте в README.md аскинему с запуском и демонстрацией различных исходов игры
Подсказки
Зависит ли реализация функции нахождения НОД от того, как использует ее вызывающий код?
"""