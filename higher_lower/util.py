from data import data
import random

def choices():
   return random.choice(data)

def game():
    while True:
        # Initial variables with the right assignments
        a = choices()
        b = choices()
        while b == a:
            b = choices()
        score = 0

        # PrintStatement to show the ones being comparable
        print(f"Compare A: {a['name']}, {a['description']}\nVS\nAgainst B: {b['name']}, {b['description']}\n")
        # Answer from the user
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        while True:
            if guess == compare(a,b):
                score += 1
                print(f"\nYou're right! Current score: {score}.\n")
                if guess == "A":
                    b = choices()
                    while b == a:
                        b = choices()
                    print(f"Compare A: {a['name']}\nVS\nAgainst B: {b['name']}\n")
                    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
                else:
                    a = b
                    b = choices()
                    while b == a:
                        b = choices()
                    print(f"Compare A: {a['name']}\nVS\nAgainst B: {b['name']}\n")
                    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
            else:
                print(f"You are wrong, final score: {score}\n")
                break


        play_again = input("Do you want to play again? [Y]Yes [N]No\n").upper()
        if play_again == "N":
            break


def compare(one, two):
    """Pass the follow persons, 'A' and 'B'"""
    if one['follower_count'] > two['follower_count']:
        return "A"
    else:
        return "B"