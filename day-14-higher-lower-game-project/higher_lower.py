# Display ASCII art
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Takes the user's guess and the follower counts and returns if they got it
    right."""
    if a_followers > b_followers:
        return user_guess == "a"  # if A has more followers and the user guessed A, return True
    else:
        return user_guess == "b"  # if B has more followers and the user guessed B, return True


print(logo)
score = 0
game_should_continue = True
# Generate a random account for account_b to be used by account_a
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Make the account at position B become the next account at position A
    account_a = account_b
    # Generate a random account for account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"... against B: {format_data(account_b)}.")
    
    
    # Ask the user for a guess (e.g., "Guess who has more followers?")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Clear the screen
    print("\n" * 20)
    print(logo)
    
    # Check if user is correct
    ## Get follower account of each account
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    
    ## Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    
    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
