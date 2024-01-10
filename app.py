import tkinter as tk
from tkinter import messagebox
from guess_number_game import GuessNumberGame

def on_guess():
    try:
        user_guess = int(entry_guess.get())
        result = game.guess(user_guess)
        if result == "Correct":
            messagebox.showinfo("Guess the Number", f"Correct! It took you {game.guesses} guesses.")
            game.reset_game()
        else:
            label_hint.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the game instance
game = GuessNumberGame()

# Create the main window
root = tk.Tk()
root.title("Guess the Number Game")

# Set window size (width x height)
root.geometry("400x300")

# Create and place widgets
label_instruction = tk.Label(root, text="Guess a number between 1 and 100")
label_instruction.pack()

entry_guess = tk.Entry(root)
entry_guess.pack()

button_guess = tk.Button(root, text="Guess", command=on_guess)
button_guess.pack()

label_hint = tk.Label(root, text="")
label_hint.pack()

# Start the GUI event loop
root.mainloop()
