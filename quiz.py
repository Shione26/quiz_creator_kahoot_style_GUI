# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

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

# randomize the question order
# create the main window
# display one question and its choices
# check user input
# give feedback whether the answer is correct or not
# loop through the randomized questions list
# track score
# display score at the end