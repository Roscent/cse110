import random

def main():
    print("Welcome to the word guessing game!\n")
    
    # List of possible secret words (can be expanded)
    word_list = ["mosiah", "alma", "nephi", "helaman", "moroni", "abinadi", "ammon", "ether"]
    secret_word = random.choice(word_list)
    max_guesses = 10
    guess_count = 0
    
    # Generate initial hint
    initial_hint = "_ " * len(secret_word)
    print(f"Your hint is: {initial_hint}")
    
    while guess_count < max_guesses:
        # Get user's guess and convert to lowercase
        guess = input("What is your guess? ").lower()
        guess_count += 1
        
        # Check if guess has correct length
        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have {len(secret_word)} letters.\n")
            continue
        
        # Check if guess is correct
        if guess == secret_word:
            print(f"Congratulations! You guessed it!")
            print(f"It took you {guess_count} guesses.")
            return
        
        # Generate hint for incorrect guess
        hint = []
        for i in range(len(secret_word)):
            guess_char = guess[i]
            if guess_char == secret_word[i]:
                hint.append(guess_char.upper())
            elif guess_char in secret_word:
                hint.append(guess_char.lower())
            else:
                hint.append("_")
        
        # Format hint with spaces between characters
        formatted_hint = " ".join(hint)
        print(f"Your hint is: {formatted_hint}\n")
    
    # If loop completes without correct guess
    print(f"Sorry, you've used all {max_guesses} guesses.")
    print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    main()