#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from brain_games.asker import ask_three_times
from brain_games.games.progression import progression_randoms


name = main()
print('What number is missing in the progression?')
progression_randoms = [progression_randoms() for _ in range(3)]
ask_three_times(progression_randoms, name)
