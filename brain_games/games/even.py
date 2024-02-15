import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)

    def is_even(number):
        return False if number % 2 else True
    answer = "yes" if is_even(number) else "no"
    return str(number), answer
