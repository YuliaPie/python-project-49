import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def randoms():
    number = random.randint(1, 100)
    if number % 2 == 0:
        correct_answer = "yes"
    if number % 2 != 0:
        correct_answer = "no"
    question = f"{number}"
    return question, correct_answer
