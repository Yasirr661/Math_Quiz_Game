# Math_Quiz_Game
#The program should teach the children how to answer addition and subtraction questions correctly


import random


def show_question(current_level):
    if current_level == 1:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
    elif current_level == 2:
        num1 = random.randint(21, 40)
        num2 = random.randint(21, 40)
    elif current_level == 3:
        num1 = random.randint(41, 60)
        num2 = random.randint(41, 60)
    elif current_level == 4:
        num1 = random.randint(61, 80)
        num2 = random.randint(61, 80)
    elif current_level == 5:
        num1 = random.randint(81, 100)
        num2 = random.randint(81, 100)

    # Swap operands if right operand is greater than left operand
    if num2 > num1:
        num1, num2 = num2, num1

    # (1) - Both operands are even
    if num1 % 2 == 0 and num2 % 2 == 0:
        question_type = 1
    # (2) - Both operands are odd
    elif num1 % 2 == 1 and num2 % 2 == 1:
        question_type = 2
    else:
        question_type = 3

    random_symbols = generate_operator(1)

    if question_type == 1:
        question_header = "{} {} {} = ?".format(num1, random_symbols, num2)
        if random_symbols == '+':
            answer = num1 + num2
        else:
            answer = num1 - num2
    elif question_type == 2:
        question_header = "{} {} {} = ?".format(num1, random_symbols, num2)
        if random_symbols == '+':
            answer = num1 + num2
        else:
            answer = num1 - num2
    else:
        question_header = "{} {} {} = ?".format(num1, random_symbols, num2)
        if random_symbols == '+':
            answer = num1 + num2
        else:
            answer = num1 - num2

    return (question_header, answer)


def generate_operator(length):
    operators = ['+', '-']
    return ''.join(random.choice(operators) for i in range(length))


def get_possible_wrong_answers(answer,level):
    if level == 1:
        max_value = 40
    elif level == 2:
        max_value = 80
    else:
        max_value = 100
    possible_wrong_answers = [answer - 2, answer - 1, answer + 1, answer + 2]
    new_possible_wrong_answers = []
    for x in possible_wrong_answers:
        if 1 <= x <= max_value:
            new_possible_wrong_answers.append(x)
    return new_possible_wrong_answers


def choices():
    rounds = 5
    current_round = 1
    current_level = 1
    current_type = 1
    correct_answers = 0

    while current_round <= rounds:
        for question_type in range(1, 4):
            if current_type != question_type:
                continue

            # print current level before first question of each level
            if correct_answers == 0:
                print("\n# Level:", current_level,"\n")

            while True:
                question, answer = show_question(current_level)
                print(question)

                # get possible wrong answers
                possible_wrong_answers = get_possible_wrong_answers(answer, level=current_level)

                # check if answer is in possible wrong answers
                if answer in possible_wrong_answers:
                    possible_wrong_answers.remove(answer)

                # Shuffle the list of possible wrong answers
                random.shuffle(possible_wrong_answers)

                # Take the first two elements of the shuffled list to use as wrong answers
                if len(possible_wrong_answers) >= 2:
                    wrong_answer_1 = possible_wrong_answers[0]
                    wrong_answer_2 = possible_wrong_answers[1]
                else:
                    # handle case where possible_wrong_answers has less than 2 elements
                    wrong_answer_1 = answer + 1
                    wrong_answer_2 = answer - 1

                # Shuffle the order of the answer choices
                answer_choices = [answer, wrong_answer_1, wrong_answer_2]
                random.shuffle(answer_choices)

                # Assign each answer choice to a letter (A, B, or C)
                a = answer_choices[0]
                b = answer_choices[1]
                c = answer_choices[2]

                # Print the answer choices
                print("Select correct answer:")
                print("A) {} \nB) {} \nC) {}".format(a, b, c))

                # Ask the user to enter their answer
                user_answer = input("Enter your answer (A, B, or C): ").upper()

                # Check if the user's answer is correct
                if user_answer == '0':
                    print("See You Soon (;")
                    return
                if user_answer == 'A' and a == answer:
                    print("\nWell done!! Your answer is correct :) \n")
                    correct_answers += 1
                    break
                elif user_answer == 'B' and b == answer:
                    print("\nWell done!! Your answer is correct :) \n")
                    correct_answers += 1
                    break
                elif user_answer == 'C' and c == answer:
                    print("\nWell done!! Your answer is correct :) \n")
                    correct_answers += 1
                    break
                else:
                    print("\nIncorrect answer :(.")
                    print("The correct answer is", answer)

            current_type = (current_type % 3) + 1

            # check if level needs to be increased
            if correct_answers == 3:
                current_level += 1
                correct_answers = 0
                break

        current_round += 1





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def run_all_functions():
    global random_symbols
    random_symbols = generate_operator(1)  # generate a single operator
    choices()


run_all_functions()
