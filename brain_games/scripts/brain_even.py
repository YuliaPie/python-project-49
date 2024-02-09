#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times
from brain_games.games.even import even_randoms


name = main()
print('Answer "yes" if the number is even, otherwise answer "no".')
even_randoms = [even_randoms() for _ in range(3)]
ask_three_times(even_randoms, name)
