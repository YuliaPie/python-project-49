import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)
    answer = ""
    if number == 1:
        answer = "no"
    root = int(number ** 0.5)
    possible_deviders = list(range(2, root + 1))
    for n in possible_deviders:
        if number % n == 0:
            answer = "no"
            break
    if answer != "no":
        answer = "yes"
    return str(number), answer
