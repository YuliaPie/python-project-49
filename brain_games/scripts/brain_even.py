#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import main

name = main()
print('Answer "yes" if the number is even, otherwise answer "no".')
correct_answer_counter = 0
while correct_answer_counter < 3:
    number = random.randint(1, 100)
    print(f"Question: {number}")
    answer = input("Your answer: ")
    if number % 2 == 0:
        correct_answer = "yes"
    if number % 2 != 0:
        correct_answer = "no"
    if answer == correct_answer:
        correct_answer_counter += 1
        print("Correct!")
        if correct_answer_counter == 3:
            print(f"Congratulations, {str(name)}!")
            exit()

    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
        print(f"Let's try again, {str(name)}!")
        correct_answer_counter = 0
        exit()
