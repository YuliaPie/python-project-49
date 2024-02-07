#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times

name = main()
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_randoms():
    number = random.randint(1, 100)
    if number % 2 == 0:
        correct_answer = "yes"
    if number % 2 != 0:
        correct_answer = "no"
    question = f"{number}"
    return [question, correct_answer]


ask_three_times([even_randoms(), even_randoms(), even_randoms()], name)
