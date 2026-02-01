import json
import os

menu_display = """
╔════════════════════════════════╗
║       ☕ Coffee Menu ☕       ║
╠════════════════════╦═══════════╣
║ $ 1.50             ║ Expresso  ║
║ $ 2.50             ║ Latte     ║
║ $ 3.00             ║ Cappuccino║
╚════════════════════╩═══════════╝
"""

menu = {
    "expresso":
        {
            "ingredients":
                {
                    "water": 50,
                    "coffee": 18,
                },
            "cost": 1.5,
        },
    "latte":
        {
            "ingredients":
                {
                    "water": 200,
                    "coffee": 24,
                    "milk": 150,
                },
            "cost": 2.50,
        },
    "Cappuccino":
        {
            "ingredients":
                {
                    "water": 250,
                    "coffee": 24,
                    "milk": 100,
                },
            "cost": 3.00,
        }
}

content = {
    "water" : 500,
    "coffee": 200,
    "milk" : 400,
}

# Name of my json file
COINS_FILE = "coins.json"

# Method to save the coin values on the json file
def save_coins(coins):
    with open(COINS_FILE, "w") as file:
        json.dump(coins, file)

def load_coins():
    if os.path.exists(COINS_FILE):
        with open(COINS_FILE, "r") as file:
            return json.load(file)
    else:
        return {
            "quarters": 0,
            "dimes": 0,
            "nickles": 0,
            "pennies": 0,
        }

def report(coins):
    for item, amount in content.items():
        if item == "coffee":
            print(f"{item} = {amount}g")
        else:
            print(f"{item} = {amount}ml")

    for coin, value in coins.items():
        print(f"{coin}: {value}")

def working(option, coins):
    if option == "espresso":
        print("Please insert coins.")

    for coin in coins:
        while True:
            coins[coin] += int(input(f"How much {coin}? "))
            if coins[coin] < 0:
                print("It can't be negative. Try again.")
            else:
                break
    save_coins(coins)
