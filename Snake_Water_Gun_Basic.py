import random
from tkinter import *

# Game logic function
def play_game(user_choice):
    options = ["Snake", "Water", "Gun"]
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Snake" and computer_choice == "Water") or (user_choice == "Water" and computer_choice == "Gun") or (user_choice == "Gun" and computer_choice == "Snake"):
        result = "You won!"
    else:
        result = "You lost!"

    result_label.configure(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}")


# Function to handle user input
def get_user_input():
    user_choice = input_var.get()
    play_game(user_choice)

# Create Tkinter window
window = Tk()
window.title("Snake Water Gun")

# Label and Entry for user input
input_label = Label(window, text="OPTIONS: Choose S for Snake, W for Water, G for Gun")
input_label.pack()

input_var = StringVar()
input_entry = Entry(window, textvariable=input_var)
input_entry.pack()

# Button to submit user input
submit_button = Button(window, text="Submit", command=get_user_input)
submit_button.pack()

# Result label
result_label = Label(window)
result_label.pack()

# Start Tkinter event loop
window.mainloop()
