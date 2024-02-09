import random


TASK = 'What is the result of the expression?.'


def randoms():
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
    return question, str(correct_answer)
