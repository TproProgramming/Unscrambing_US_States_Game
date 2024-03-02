import random

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

def scramble_word(word):
    # Remove spaces from the word
    word = word.replace(" ", "")
    # Convert word to a list of characters
    chars = list(word)
    # Shuffle the list
    random.shuffle(chars)
    # Convert the list back to a string
    return ''.join(chars)

def choose_random_state(used_states):
    remaining_states = set(us_states) - used_states
    if not remaining_states:
        return None  # All states have been guessed
    return random.choice(list(remaining_states))

def main():
    used_states = set()
    correct_guesses = 0
    incorrect_guesses = 0
    
    while len(used_states) < len(us_states):
        state = choose_random_state(used_states)
        if state is None:
            print("Congratulations! You have guessed all 50 states.")
            break
        
        used_states.add(state)
        scrambled_state = scramble_word(state.lower())
        print("Guess the US state:")
        print(scrambled_state)

        guess = input("Your guess (type 'exit' to quit): ").strip().lower()

        if guess == "exit":
            print("Exiting the game. Thanks for playing!")
            break
        
        if guess == state.lower():
            print("Correct! The state is", state)
            correct_guesses += 1
        else:
            print("Incorrect. The correct answer is", state)
            incorrect_guesses += 1
        
        print("Correct guesses:", correct_guesses)
        print("Incorrect guesses:", incorrect_guesses)
        print()

if __name__ == "__main__":
    main()
