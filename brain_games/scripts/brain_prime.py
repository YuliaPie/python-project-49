#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times


name = main()
def prime_randoms():
    number = random.randint(1, 100)
    answer = ""
    if number == 1:
        answer = "no"
    root = int(number ** 0.5)
    possible_deviders = list(range(2, root+1))
    for n in possible_deviders:
        if number % n == 0:
            answer = "no"
            break
    if answer != "no":
        answer = "yes"
    return [str(number), answer]
prime_randoms = [prime_randoms(), prime_randoms(), prime_randoms()]
ask_three_times(prime_randoms, name)