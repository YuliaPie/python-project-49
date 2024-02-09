#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times
from brain_games.games.prime import prime_randoms

name = main()
print('Answer "yes" if the number is prime, otherwise answer "no".')
prime_randoms = [prime_randoms() for _ in range(3)]
ask_three_times(prime_randoms, name)