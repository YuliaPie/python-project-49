#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times
from brain_games.games.gcd import gcd_randoms

name = main()
print('Find the greatest common divisor of given numbers.')
gcd_randoms = [gcd_randoms() for _ in range(3)]
ask_three_times(gcd_randoms, name)
