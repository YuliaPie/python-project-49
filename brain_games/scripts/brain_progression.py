#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times


name = main()
print('What number is missing in the progression?')
def progression_randoms():
    first_number = random.randint(1, 20)
    step = random.randint(1, 5)
    progression = [first_number]
    for n in range(10):
        progression.append(progression[-1] + step)
    hidden_index = random.randint(0, 9)
    answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = (' '.join(map(str, progression)))
    return [question, answer]

progression_randoms = [progression_randoms(),progression_randoms(),progression_randoms()]
ask_three_times(progression_randoms, name)