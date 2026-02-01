import contentCM as Cm
from CoffeeMachine.contentCM import working

# ToDo - I need to start implementing the logic of the machine

coins = Cm.load_coins()

while True:
        # Chose the type of coffee
    print(Cm.menu_display)

    answer = str(input("What do you like? (Espresso, Cappuccino or Latte)\n")).lower()
    valueAnswers = ["espresso", "cappuccino", "latte", "report", "off"]

    while answer not in valueAnswers:
        answer = str(input("Not a value option, please select between: Espresso, Cappuccino or Latte\n"))

    captWord = answer.capitalize()
    print(f"You chose: {captWord}")

    if answer == "report":
        Cm.report(coins)

    # Stops the machine from working, like a shutdown
    elif answer == "off":
        print("The machine is shutting down...")
        break
        # Cases
    else:
        working(answer, coins)

    # Information about the status of items and money
