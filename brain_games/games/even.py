import random


def even_randoms():
    number = random.randint(1, 100)
    if number % 2 == 0:
        correct_answer = "yes"
    if number % 2 != 0:
        correct_answer = "no"
    question = f"{number}"
    return [question, correct_answer]
