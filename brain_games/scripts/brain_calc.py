#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times
from brain_games.games.calc import calc_randoms


name = main()
print('What is the result of the expression?')
calc_randoms = [calc_randoms() for _ in range(3)]
ask_three_times(calc_randoms, name)
