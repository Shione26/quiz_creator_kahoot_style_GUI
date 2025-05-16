# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

import random

# read the file
filename = input("Enter the filename (e.g. name.txt): ")
with open(filename, "r") as file:
    lines = [line.strip() for line in file if line.strip() != ""]
# store the data
quiz_data = []

# create a block of 6 lines for each question
for i in range(0, len(lines), 6):
    question_line = lines[i]
    choice_a = lines[i + 1]
    choice_b = lines[i + 2]
    choice_c = lines[i + 3]
    choice_d = lines[i + 4]
    answer_line = lines[i + 5]

    # extract actual text
    question = question_line.replace("Question: ", "")
    a = choice_a.replace("a. ", "")
    b = choice_b.replace("b. ", "")
    c = choice_c.replace("c. ", "")
    d = choice_d.replace("d. ", "")
    correct_letter = answer_line.replace("Correct answer:", "").strip().upper()

    # store choices in a list
    choices = [a, b, c, d]

    # figure out the correct answer using the position of the letter
    letter_index = ["A", "B", "C", "D"].index(correct_letter)
    correct_answer = choices[letter_index]

    # add to the quiz data list
    quiz_data.append({
        "question": question,
        "options": choices,
        "answer": correct_answer
    })

# randomize the question order
shuffled_quiz = random.sample(quiz_data, len(quiz_data))
print(shuffled_quiz)

# create the main window
# display one question and its choices
# check user input
# give feedback whether the answer is correct or not
# loop through the randomized questions list
# track score
# display score at the end