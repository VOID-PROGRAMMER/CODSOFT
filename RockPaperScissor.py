import tkinter as tk
import random
from tkinter import messagebox

# Initialize the scoreboard globally
a = 0
b = 0

def play_game(user_choice):
    global a, b
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        result = "You Win!"
        a += 1
    else:
        result = "Computer Wins!"
        b += 1

    # Update the scoreboard immediately
    scoreboard = f"[You: {a}, Computer: {b}]"

    return f"Computer's Choice: {computer_choice}\n{result}\n{scoreboard}"

def on_button_click(user_choice, result_label):
    result = play_game(user_choice)
    result_label.config(text=result)

    # Ask the user if they want to play again
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    
    if not play_again:
        # If the user chooses not to play again, thank them for playing and close the application
        messagebox.showinfo("Thanks for Playing!", "Thanks for playing! Closing the game.")
        root.destroy()

def create_gui():
    global root
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    # Add a welcome message
    welcome_label = tk.Label(root, text="Welcome to Rock, Paper, Scissors Game!", font=("Helvetica", 14, "bold"))
    welcome_label.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=20)

    for choice in ["Rock", "Paper", "Scissor"]:
        button = tk.Button(root, text=choice, font=("Helvetica", 12), width=10, height=2, command=lambda ch=choice: on_button_click(ch, result_label))
        button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()