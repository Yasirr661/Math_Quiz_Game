

This code is a **quiz game** that generates arithmetic questions of different types and levels for the user to solve. It also provides the user with three answer choices, one of which is correct. The user is given five rounds to answer the questions. After each round, if the user has correctly answered three questions, they move on to the next level. The code consists of four functions: show_question, generate_operator, get_possible_wrong_answers, and choices.

***show_question(current_level)*** : This function takes the current level as an argument and generates an arithmetic question of one of the three types (both operands are even, both operands are odd, or one operand is even and the other is odd) with random operands within the range of the current level. It also generates a random operator (+ or -) and returns the question header and the correct answer as a tuple.

***generate_operator(length)*** : This function takes a length as an argument (in this case, always 1) and returns a random operator (+ or -) of that length.

***get_possible_wrong_answers(answer,level)*** : This function takes the correct answer and the current level as arguments and generates a list of four possible wrong answers. It then filters out any answer less than 1 or greater than the maximum value of the current level and returns the remaining wrong answers as a list.

***choices()*** : This function is the main function that runs the quiz game. It sets the number of rounds, the current round, the current level, the current type, and the number of correct answers to 0. It then starts a while loop that runs until the current round is greater than the number of rounds. Within this loop, it loops through the three question types (1, 2, and 3) and generates questions of that type. It then prints the current level before the first question of each level. It then asks the user to enter their answer and checks if the answer is correct. If the user's answer is correct, it increments the number of correct answers and breaks out of the loop for the current question type. If the user's answer is incorrect, it prints a message and continues to the next question of the same type. After all questions of a given type have been answered, it checks if the user has answered three questions correctly. If so, it increments the current level and sets the number of correct answers to 0. It then moves on to the next round.



### Program Flow :
1- The program starts with the choices() function.
2- choices() initializes the game by setting the number of rounds, the current round, level, type, and the number of correct answers to 0.
3- choices() enters a while loop that runs until the current round equals the number of rounds.
4- Within the while loop, choices() enters a for loop that iterates over three question types.
5- If the current type is not equal to the question type, the loop continues to the next iteration.
6- The show_question() function is called to generate a new question based on the current level and question type.
7- The question and answer are printed to the console.
8- The get_possible_wrong_answers() function is called to generate a list of possible wrong answers based on the current level and answer.
9- The list of possible wrong answers is shuffled and the first two elements are selected as wrong answers.
10- The answer choices (including the correct answer and two wrong answers) are shuffled and assigned letters (A, B, and C).
11- The answer choices are printed to the console.
12-cThe user is prompted to enter their answer (A, B, or C).
13- If the user enters '0', the program ends.
14- If the user's answer is correct, the program prints a success message and increments the number of correct answers.
15- If the user's answer is incorrect, the program prints a failure message and loops back to step 6.
16- Once the for loop has completed all three question types, the choices() function increments the current round and sets the current type to 1.
17- If the number of correct answers is equal to the number of rounds, the program prints a success message and ends. Otherwise, the program loops back to step 5.

