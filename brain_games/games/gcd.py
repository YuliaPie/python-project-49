import random


TASK = "Find the greatest common divisor of given numbers."


def randoms():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    question = f"{first} {second}"
    randoms = [first, second]
    randoms.sort()
    first = randoms[0]
    second = randoms[1]
    devider = first
    while True:
        if second % devider == 0 and first % devider == 0:
            return question, str(devider)
        else:
            devider -= 1
