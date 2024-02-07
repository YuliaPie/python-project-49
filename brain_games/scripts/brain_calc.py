#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times

name = main()
print('What is the result of the expression?')


def calc_randoms():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    operation = random.choices("+-*")
    if operation[0] == "+":
        correct_answer = first + second
    if operation[0] == "-":
        correct_answer = first - second
    if operation[0] == "*":
        correct_answer = first * second
    question = f"{first} {operation[0]} {second}"
    return [question, correct_answer]


calc_randoms = [calc_randoms(), calc_randoms(), calc_randoms()]
ask_three_times(calc_randoms, name)
