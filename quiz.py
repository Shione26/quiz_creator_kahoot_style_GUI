# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

from tkinter import *
import random

# read the file
filename = input("Enter the filename (e.g. name.txt): ")
with open(filename, "r") as file:
    lines = [line.strip() for line in file if line.strip() != ""]
# store the data
quiz_data = []

# create a block of 6 lines for each question
for index in range(0, len(lines), 6):
    question_line = lines[index]
    choice_a = lines[index + 1]
    choice_b = lines[index + 2]
    choice_c = lines[index + 3]
    choice_d = lines[index + 4]
    answer_line = lines[index + 5]

    # extract actual text
    question = question_line.replace("Question: ", "")
    option_a = choice_a.replace("a. ", "")
    option_b = choice_b.replace("b. ", "")
    option_c = choice_c.replace("c. ", "")
    option_d = choice_d.replace("d. ", "")
    correct_letter = answer_line.replace("Correct answer:", "").strip().upper()

    # store choices in a list
    choices = [option_a, option_b, option_c, option_d]

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
current_question_index = 0
score = 0   # track score

# loop through the randomized questions list

# create the main window
window = Tk()

window.title(filename)
window.geometry("700x380")
window.config(bg="#f2f2f2")

# create the question label
question_label = Label(window, text="", font=("Montserrat Black", 11, "bold"), bg="white", height=2)
question_label.pack(fill="x")

image = PhotoImage(file="image.png").subsample(5, 5)
image_label = Label(window, image=image)
image_label.pack() 

# create the buttons
red_button = Button(window, text="", font=("Montserrat Black", 10, "bold"), bg="#e21b3c", fg="white", height=3, padx=165, anchor="center")
red_button.place(x=0, y=260)

blue_button = Button(window, text="", font=("Montserrat Black", 10, "bold"), bg="#1368ce", fg="white", height=3, padx=159, anchor="center")
blue_button.place(x=350, y=260)

orange_button = Button(window, text="", font=("Montserrat Black", 10, "bold"), bg="#d89e0a", fg="white", height=3, padx=165, anchor="center")
orange_button.place(x=0, y=320)

green_button = Button(window, text="", font=("Montserrat Black", 10, "bold"), bg="#298a11", fg="white", height=3, padx=165, anchor="center")
green_button.place(x=350, y=320)

# create the feedback label
feedback_label = Label(window, text="", font=("Montserrat Black", 11, "bold"), bg="#f2f2f2", fg="black")
feedback_label.pack()

# function to handle the answer selection
def handle_answer(selected_text):
    global current_question_index, score

    # check user input
    correct = shuffled_quiz[current_question_index]["answer"]
    if selected_text == correct:
        score += 1
        feedback_label.config(text="✅ Correct!", fg="green") # give feedback whether the answer is correct or not
    else:
        feedback_label.config(text=f"❌ Wrong! Correct answer: {correct}", fg="red")

    # to check if there is more question next
    current_question_index += 1
    if current_question_index < len(shuffled_quiz):
        window.after(1000, show_question)
    else:
        window.after(1000, show_result) 

# display score at the end
def show_result():
    question_label.config(text="Quiz Finished!")
    red_button.place_forget()  # removing the buttons
    blue_button.place_forget() 
    orange_button.place_forget()
    green_button.place_forget()
    feedback_label.config(text=f"Your Score: {score}/{len(shuffled_quiz)}", fg="blue")

# display one question and its choices
def show_question():
    question = shuffled_quiz[current_question_index]
    question_label.config(text=question["question"])
    feedback_label.config(text="")

    red_button.config(text=question["options"][0], command=lambda: handle_answer(question["options"][0]))
    blue_button.config(text=question["options"][1], command=lambda: handle_answer(question["options"][1]))
    green_button.config(text=question["options"][2], command=lambda: handle_answer(question["options"][2]))
    orange_button.config(text=question["options"][3], command=lambda: handle_answer(question["options"][3]))

show_question()
window.mainloop()