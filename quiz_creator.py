# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

# Import tkinter and create the main window

from tkinter import *

window = Tk()
window.geometry("700x500")  # Edit the window title, size, icon, and background
window.title("Quiz Creator")
icon = PhotoImage(file="Kahoot_Logo.png")
window.iconphoto(True, icon)

bg_image = PhotoImage(file="bg_image.png").subsample(4, 4)
bg_label = Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create entry widget for the question
question = Entry(
    window, 
    font=("Montserrat", 10), 
    bg="#f2f2f2", 
    fg="#333333", 
    width=60, 
    justify="center"
)
question.place(x=130, y=50)

window.mainloop()

# Create entry widget for options
# Create entry widget for the correct answer
# Create button for submit
# Display save message using messagebox module
# Create Exit Program
# Open a text file for writing or appending the inputs
# Append the inputs into the text file

