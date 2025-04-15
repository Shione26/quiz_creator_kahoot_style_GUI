# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

# Import tkinter and create the main window

from tkinter import *
from tkinter import messagebox 

window = Tk()
window.geometry("700x500")  # Edit the window title, size, icon, and background
window.title("Quiz Creator")
icon = PhotoImage(file="Kahoot_Logo.png")
window.iconphoto(True, icon)

bg_image = PhotoImage(file="bg_image.png").subsample(4, 4)
bg_label = Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

kahoot_photo = PhotoImage(file="kahoot.png").subsample(5, 5)
kahoot_label = Label(window, image=kahoot_photo)
kahoot_label.place(x=150, y=75)

title = Label(window, text="Quiz Creator", fg="black")
title.place(x=320, y=5 )

def user_clicks_textbox(event):
    if question.get() == question_placeholder:
        question.delete(0, END)
        question.config(fg="black")

def user_clicks_away(event):
    if question.get() == "":
        question.insert(0, question_placeholder)
        question.config(fg="gray")

# Create entry widget for the question
question_placeholder = "Start typing your question"

question = Entry(
    window, 
    font=("Montserrat", 10), 
    bg="#f2f2f2", 
    fg="#333333", 
    width=60, 
    justify="center"
)
question.insert(0, question_placeholder)
question.bind("<FocusIn>", user_clicks_textbox)
question.bind("<FocusOut>", user_clicks_away)
question.place(x=130, y=50)

# Create entry widget for options
options_photo = PhotoImage(file="choices.png").subsample(2, 2)
options_label = Label(window, image=options_photo)
options_label.place(x=40, y=300)

def focus_in_option(event):
    # If the text in the entry is a placeholder,
    if event.widget.get() in option_placeholders:   
        event.widget.delete(0, END)         # delete from the start to end
        event.widget.config(fg="black")     # and set text color to black

def focus_out_option(event):
    # If the text in the entry is empty, 
    if event.widget.get() == "":
        index = option_entries.index(event.widget)              # Find which entry widget triggered the event
        event.widget.insert(0, option_placeholders[index])      # reappear the placeholder
        event.widget.config(fg="gray")       # and set text color to gray

option_placeholders = ["Add answer 1 (A)", "Add answer 2 (B)", "Add answer 3 (C)", "Add answer 4 (D)"]  # list of placeholders

# Create entry widget for options
def create_option_entry(x, y, placeholder):
    option = Entry(
        window, 
        font=("Montserrat", 10), 
        bg="white", 
        fg="gray", 
        width=33, 
        justify="center"
    )
    option.insert(0, placeholder)   # Insert the placeholder text
    option.bind("<FocusIn>", focus_in_option)   # Bind when entry is clicked
    option.bind("<FocusOut>", focus_out_option) # Bind when user clicks away
    option.place(x=x, y=y)
    return option

# Coordinates of the 4 entry widgets and their corresponding placeholders in the list
option_entries = [
    create_option_entry(80, 331, option_placeholders[0]),
    create_option_entry(398, 331, option_placeholders[1]), 
    create_option_entry(80, 400, option_placeholders[2]),
    create_option_entry(398, 400, option_placeholders[3]),
]

correct_ans_placeholder = "Correct Answer"

def focus_in_correct_ans(event):
    if correct_ans.get() == correct_ans_placeholder:
        correct_ans.delete(0, END)
        correct_ans.config(fg="black")

def focus_out_correct_ans(event):
    if correct_ans.get() == "":
        correct_ans.insert(0, correct_ans_placeholder)
        correct_ans.config(fg="gray")

# Create entry widget for the correct answer
correct_ans = Entry(
    window, 
    font=("Montserrat", 10), 
    bg="#fff7e6", 
    fg="gray", 
    width=17, 
    justify="center"
)
correct_ans.insert(0, correct_ans_placeholder)
correct_ans.bind("<FocusIn>", focus_in_correct_ans)
correct_ans.bind("<FocusOut>", focus_out_correct_ans)
correct_ans.place(x=550, y=270)

# Open a text file for writing or appending the inputs
def submit_inputs():
    name = filename_entry.get()     # for every new entry of filename, there'll be new text files
    if name == filename_placeholder or name.strip() == "":
        messagebox.showwarning("Missing Filename", "Please enter a filename.")
        return

    correct = correct_ans.get().strip().upper()
    if correct == "":
        messagebox.showerror("Invalid Input", "Please enter the correct answer")
        return

    file = open(name + ".txt", "a")     # Append the inputs into the text file
    file.write("Question: " + question.get() + "\n")
    file.write("a. " + option_entries[0].get() + "\n")
    file.write("b. " + option_entries[1].get() + "\n")
    file.write("c. " + option_entries[2].get() + "\n")
    file.write("d. " + option_entries[3].get() + "\n")
    file.write("Correct answer:" + correct_ans.get() + "\n\n")
    file.close()
    messagebox.showinfo("Notice", "Item saved successfully!")    # Display save message using messagebox module
    reset_fields()

def reset_fields():
    question.delete(0, END)  
    for entry in option_entries:
        entry.delete(0, END) 
    correct_ans.delete(0, END)

# Placeholder for filename entry
filename_placeholder = "Enter filename here"

def focus_in_filename(event):
    if filename_entry.get() == filename_placeholder:
        filename_entry.delete(0, END)
        filename_entry.config(fg="black")

def focus_out_filename(event):
    if filename_entry.get() == "":
        filename_entry.insert(0, filename_placeholder)
        filename_entry.config(fg="gray")

# Create filename entry widget
filename_entry = Entry(
    window,
    font=("Montserrat", 10),
    bg="white",
    fg="#333333",
    width=30,
    justify="center"
)
filename_entry.insert(0, filename_placeholder)
filename_entry.bind("<FocusIn>", focus_in_filename)
filename_entry.bind("<FocusOut>", focus_out_filename)
filename_entry.place(x=245, y=28)  

# Create button for submit
submit_button = Button(window, text="Submit", font=("Montserrat", 10), command=submit_inputs)
submit_button.place(x=360, y=460)

# Create Exit Program
def exit_program():
    if messagebox.askyesno("Notice", "Are you sure you want to exit?"):
        window.destroy()

# Create button for exit program
exit_button = Button(window, text="Exit", font=("Montserrat", 10), command=exit_program)
exit_button.place(x=320, y=460)

window.mainloop()
