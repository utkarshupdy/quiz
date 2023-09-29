import tkinter as tk
import random

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Quiz")

        self.lower_label = tk.Label(root, text="Lower Bound:")
        self.lower_label.pack()
        self.lower_entry = tk.Entry(root)
        self.lower_entry.pack()

        self.upper_label = tk.Label(root, text="Upper Bound:")
        self.upper_label.pack()
        self.upper_entry = tk.Entry(root)
        self.upper_entry.pack()

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

        # Create an entry field for the user to input guesses
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

    def start_quiz(self):
        lower_bound = int(self.lower_entry.get())
        upper_bound = int(self.upper_entry.get())

        if upper_bound <= lower_bound:
            self.output_label.config(text="Invalid range. Please ensure the upper bound is greater than the lower bound.")
            return

        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0

        while True:
            try:
                guess = int(self.guess_entry.get())  # Get guess from the entry field
                attempts += 1

                if guess < secret_number:
                    self.output_label.config(text="Too low! Try again.")
                elif guess > secret_number:
                    self.output_label.config(text="Too high! Try again.")
                else:
                    self.output_label.config(text=f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                    break
            except ValueError:
                self.output_label.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()
