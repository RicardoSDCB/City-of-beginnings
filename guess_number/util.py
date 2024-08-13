from random import randint


def difficult():
    """Chose the difficult and set a number of tries"""
    difficulty = input("Choose difficulty. Type \"easy\" or \"hard\":\n").lower()
    if difficulty == "hard":
        return 5
    elif difficulty == "easy":
        return 10


def play_game(attempts):
    """Set the flow of game and finish it if certain conditions were acquired"""
    lose = attempts
    pc_choice = randint(1, 100)
    print(f"CHEAT {pc_choice}")

    # Repeat the game until the end of attempts
    for i in range(attempts, 0, -1):
        choice = int(input("Make your guess: "))
        if choice > pc_choice:
            if i > 1:
                print(f"Too high.\nGuess again.\nYou have {i-1} attempts remaining to guess the number.")
            lose -= 1
        elif choice < pc_choice:
            if i > 1:
                print(f"Too low.\nGuess again.\nYou have {i-1} attempts remaining to guess the number.")
            lose -= 1
        elif choice == pc_choice:
            print(f"You got it, the number was {pc_choice}!")
            break

    # Check if the player lose the game
    if lose == 0:
        print(f"You've run out of guesses, you lose. The number was {pc_choice}")


def game():
    """Start game and check if continue"""
    while True:
        player_dif = difficult()
        play_game(player_dif)

        again = input("Play again? 'yes' or 'no'\n").lower()
        if again == 'no':
            break
