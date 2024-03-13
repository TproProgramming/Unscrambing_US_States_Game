import random
import tkinter as tk

# List of US states
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

class USStateGame:
    def __init__(self, root):
        self.root = root
        self.root.title("US State Guessing Game")
        self.root.geometry("400x300")  # Set the initial size of the window
        self.used_states = set()
        self.correct_guesses = 0
        self.incorrect_guesses = 0
        self.current_state = ""
        self.scrambled_state = ""
        
        self.label = tk.Label(root, text="")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        self.guesses_label = tk.Label(root, text="")
        self.guesses_label.pack()

        self.new_game()

    def new_game(self):
        self.used_states.clear()
        self.correct_guesses = 0
        self.incorrect_guesses = 0
        self.next_state()

    def next_state(self):
        self.current_state = self.choose_random_state()
        if self.current_state is None:
            self.label.config(text="Congratulations! You have guessed all 50 states.")
            self.entry.config(state="disabled")
            self.submit_button.config(state="disabled")
        else:
            self.scrambled_state = self.scramble_word(self.current_state.lower())
            self.label.config(text=self.scrambled_state)
            self.update_guesses_label()

    def choose_random_state(self):
        remaining_states = set(us_states) - self.used_states
        if not remaining_states:
            return None  # All states have been guessed
        return random.choice(list(remaining_states))

    def scramble_word(self, word):
        # Remove spaces from the word
        word = word.replace(" ", "")
        # Convert word to a list of characters
        chars = list(word)
        # Shuffle the list
        random.shuffle(chars)
        # Convert the list back to a string
        return ''.join(chars)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        if guess == "exit":
            self.root.destroy()
        elif guess == self.current_state.lower():
            self.correct_guesses += 1
            self.label.config(text=f"Correct! The state is {self.current_state}")
        else:
            self.incorrect_guesses += 1
            self.label.config(text=f"Incorrect. The correct answer is {self.current_state}")
        self.label.after(2000, self.update_score)

    def update_score(self):
        self.label.config(text=f"Correct guesses: {self.correct_guesses}\nIncorrect guesses: {self.incorrect_guesses}")
        self.entry.delete(0, tk.END)
        self.next_state()

    def update_guesses_label(self):
        self.guesses_label.config(text=f"Correct guesses: {self.correct_guesses}\nIncorrect guesses: {self.incorrect_guesses}")

def main():
    root = tk.Tk()
    game = USStateGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
