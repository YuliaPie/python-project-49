def ask_three_times(randoms, name):
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        question_answer = randoms[correct_answer_counter]
        question = question_answer[0]
        correct_answer = str(question_answer[1])
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == correct_answer:
            correct_answer_counter += 1
            print("Correct!")
            if correct_answer_counter == 3:
                print(f"Congratulations, {str(name)}!")
                exit()
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}.")
            print(f"Let's try again, {str(name)}!")
            exit()
