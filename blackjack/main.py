from util import shuffle, push
import cards_deck as cd

# Play Again?
while True:
    shuffleDeck = shuffle()
    flag = "y"
    dealer = False
    blackPlayer = False
    blackDealer = False
    # PLAYER HAND INITIAL PUSHES
    push("player")
    push("player")
    # print(f"{cd.visualPlayerHand}\nTotal = {sum(cd.logicalPlayerHand)}")
    # DEALER HAND INITIAL PUSHES
    push("dealer")
    push("dealer")
    print(f"Dealer Hand: \n{cd.visualDealerHand[0]}, ?")

    # Who won?
    while True:
        # The game
        while True:
            '''----------- PLAYER LOGIC -----------'''

            # Check for cases
            if dealer:
                break
            # Case checks with aces
            if len(cd.logicalPlayerHand) == 2:
                # Firs or second card is an ACE
                if cd.logicalPlayerHand[0] == 1 or cd.logicalPlayerHand[1] == 1:
                    # First card is an ACE
                    if cd.logicalPlayerHand[0] == 1:
                        # Second card is a 10 = BLACKJACK, the sum of these cards is 21
                        if cd.logicalPlayerHand[1] == 10:
                            print(cd.visualPlayerHand)
                            cd.logicalPlayerHand.append(10)
                            blackPlayer = True
                            # print("BLACKJACK")
                            break
                        # If the second card is not a 10
                        else:
                            print(cd.visualPlayerHand)
                            print(f"{sum(cd.logicalPlayerHand)} or {sum(cd.logicalPlayerHand) + 10}")
                            flag = input("1 Do you want another card? [Y]Yes [N]No\n").lower()

                            if flag == "n":
                                cd.logicalPlayerHand.append(10)
                                # print(f"TESTE MÃO TOTAL 1: {sum(cd.logicalPlayerHand)}")
                                break
                    # Second card is an ACE
                    elif cd.logicalPlayerHand[1] == 1:
                        # If the first card is a 10 = BLACKJACK, the sum of these cards is 21
                        if cd.logicalPlayerHand[0] == 10:
                            print(cd.visualPlayerHand)
                            cd.logicalPlayerHand.append(10)
                            blackPlayer = True
                            # print("BLACKJACK")
                            break
                        # If the second card is not a 10
                        else:
                            print(cd.visualPlayerHand)
                            print(f"{sum(cd.logicalPlayerHand)} or {sum(cd.logicalPlayerHand) + 10}")
                            flag = input("2 Do you want another card? [Y]Yes [N]No\n").lower()

                            if flag == "n":
                                cd.logicalPlayerHand.append(10)
                                # print(f"TESTE MÃO TOTAL 2: {sum(cd.logicalPlayerHand)}")
                                break
                # If none of the first cards is an ACE
                else:
                    print(cd.visualPlayerHand)
                    print(f"{sum(cd.logicalPlayerHand)}")
                    flag = input("3 Do you want another card? [Y]Yes [N]No\n").lower()

                    if flag == "n":
                        # print(f"TESTE TOTAL 3: {sum(cd.logicalPlayerHand)}")
                        break
            # Last card pushed is an ACE
            elif cd.logicalPlayerHand[-1] == 1:
                # Check the sum attribute with 10 to print the correct amount
                if sum(cd.logicalPlayerHand) + 10 > 21:
                    print(f"{sum(cd.logicalPlayerHand)}")
                    flag = input("4 Do you want another card? [Y]Yes [N]No\n").lower()

                    if flag == "n":
                        # print(f"TESTE TOTAL 4: {sum(cd.logicalPlayerHand)}")
                        break

                elif sum(cd.logicalPlayerHand) + 10 == 21:
                    cd.logicalPlayerHand.append(10)
                    # print(sum(cd.logicalPlayerHand))
                    # print(f"21! {sum(cd.logicalPlayerHand)}")
                    break

                elif sum(cd.logicalPlayerHand) + 10 < 21:
                    print(f"{sum(cd.logicalPlayerHand)} or {sum(cd.logicalPlayerHand) + 10}")
                    flag = input("5 Do you want another card? [Y]Yes [N]No\n").lower()

                    if flag == "n":
                        cd.logicalPlayerHand.append(10)
                        # print(f"TESTE MÃO TOTAL 5: {sum(cd.logicalPlayerHand)}")
                        break
            # Last card pushed is not an ACE
            else:
                print(sum(cd.logicalPlayerHand))
                if sum(cd.logicalPlayerHand) == 21:
                    # print("21!")
                    break
                elif sum(cd.logicalPlayerHand) > 21:
                    # print("More than 21....")
                    break

                flag = input("6 Do you want another card? [Y]Yes [N]No\n")

                if flag == "n":
                    # print(f"TESTE MÃO TOTAL 6: {sum(cd.logicalPlayerHand)}")
                    break

            # Check the current value of cards and keep playing
            if sum(cd.logicalPlayerHand) < 21:
                if flag == "y":
                    push("player")
                    print(f"\nDealer Hand: \n{cd.visualDealerHand[0]}, ?")
                    print("Player Hand:")
                    print(f"{cd.visualPlayerHand}")
            # else:
            #     print("More than 21...")
            #     break

        '''----------- DEALER LOGIC -----------'''
        dealer = True
        flag = "y"
        print(f"Dealer Hand:\n{cd.visualDealerHand}\n{sum(cd.logicalDealerHand)}")

        if len(cd.logicalDealerHand) == 2:
            # Firs or second card is an ACE
            if cd.logicalDealerHand[0] == 1 or cd.logicalDealerHand[1] == 1:
                # First card is an ACE
                if cd.logicalDealerHand[0] == 1:
                    # Second card is a 10 = BLACKJACK, the sum of these cards is 21
                    if cd.logicalDealerHand[1] == 10:
                        # print(cd.visualDealerHand)
                        blackDealer = True
                        cd.logicalDealerHand.append(10)
                        # print("BLACKJACK DEALER")
                        break
                    # If the second card is not a 10
                    else:
                        print(f"Dealer:\n{cd.visualDealerHand}")
                        if sum(cd.logicalDealerHand) + 10 >= 17:
                            flag = "n"
                            cd.logicalDealerHand.append(10)
                            # print(cd.visualDealerHand)
                            # print(f"TESTE MÃO TOTAL DEALER 1: {sum(cd.logicalDealerHand)}")
                            break

                        # if flag == "n":
                        #     cd.logicalDealerHand.append(10)
                        #     print(f"TESTE MÃO TOTAL 1: {sum(cd.logicalDealerHand)}")
                        #     break
                # Second card is an ACE
                elif cd.logicalDealerHand[1] == 1:
                    # If the first card is a 10 = BLACKJACK, the sum of these cards is 21
                    if cd.logicalDealerHand[0] == 10:
                        print(cd.visualDealerHand)
                        blackDealer = True
                        cd.logicalDealerHand.append(10)
                        # print("BLACKJACK DEALER")
                        break
                    # If the first card is not a 10
                    else:
                        print(cd.visualDealerHand)
                        if sum(cd.logicalDealerHand) + 10 >= 17:
                            flag = "n"
                            cd.logicalDealerHand.append(10)
                            # print(f"TESTE MÃO TOTAL DEALER 2: {sum(cd.logicalDealerHand)}")
                            break

                        # if flag == "n":
                        #     cd.logicalDealerHand.append(10)
                        #     print(f"TESTE MÃO TOTAL 2: {sum(cd.logicalDealerHand)}")
                        #     break
            # If none of the first cards is an ACE
            else:
                # print(f"Dealer Hand:\n{cd.visualDealerHand}")
                # print(f"{sum(cd.logicalDealerHand)}")
                if sum(cd.logicalDealerHand) >= 17:
                    flag = "n"
                    # print(f"TESTE MÃO TOTAL DEALER 3: {sum(cd.logicalDealerHand)}")
                    break

                # if flag == "n":
                #     print(f"TESTE TOTAL 3: {sum(cd.logicalDealerHand)}")
                #     break
        # Last card pushed is an ACE
        elif cd.logicalDealerHand[-1] == 1:
            # Check the sum attribute with 10 to print the correct amount
            if sum(cd.logicalDealerHand) + 10 > 21:
                # print(f"{sum(cd.logicalDealerHand)}")

                if sum(cd.logicalDealerHand) >= 17:
                    flag = "n"
                    # print(f"TESTE TOTAL DEALER 4: {sum(cd.logicalDealerHand)}")
                    break

            elif 21 > sum(cd.logicalDealerHand) + 10 >= 17:
                flag = "n"
                cd.logicalDealerHand.append(10)
                # print(f"TESTE MÃO TOTAL DEALER 5: {sum(cd.logicalDealerHand)}")
                break

            elif sum(cd.logicalDealerHand) + 10 == 21:
                print(cd.logicalDealerHand)
                cd.logicalDealerHand.append(10)
                # print(f"DEALER {sum(cd.logicalDealerHand)}!")
                break

        # Last card pushed is not an ACE
        else:
            # print(sum(cd.logicalDealerHand))
            if sum(cd.logicalDealerHand) == 21:
                # print(f"DEALER {sum(cd.logicalDealerHand)} CASE 2!")
                break
            elif sum(cd.logicalDealerHand) > 21:
                # print("DEALER more than 21....")
                break

            if sum(cd.logicalDealerHand) >= 17:
                # print(f"TESTE MÃO TOTAL 6: {sum(cd.logicalDealerHand)}")
                break

        # Check the current value of cards and keep playing
        if sum(cd.logicalDealerHand) < 17:
            if flag == "y":
                push("dealer")
                # print(f"\nDealer Hand: \n{cd.visualDealerHand}")
        # elif 17 <= sum(cd.logicalDealerHand) < 21:
        #     print("CAIU AQUI, VENHA VER O QUE ESTÁ OCORRENDO. LINHA 229 ATÉ ENT.")
        #     print("Dealer final Hand:")
        #     print(cd.visualDealerHand)
        #     print(f"Total Dealer Hand = {sum(cd.logicalDealerHand)}")
        #     break
        # elif sum(cd.logicalDealerHand) > 21:
        #     print("CAIU NO SEGUNDO CASO PARA VERIFICAR, ATUAL LINHA 235")
        #     print("Dealer more than 21...")
        #     break

        # print("LOGIC TO WHO WON")
        # break

    '''--------------WHO WON?----------------'''
    if blackPlayer:
        if blackDealer:
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("Draw\nYou and Dealer has a Blackjack!")
        else:
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("YOU WIN\n!!!! Blackjack !!!!")
    elif blackDealer:
        if not blackPlayer:
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("You lose\n!!!! Dealer Blackjack !!!!")
    elif sum(cd.logicalPlayerHand) > 21:
        if sum(cd.logicalDealerHand) <= 21:
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("You lose 1")
        elif sum(cd.logicalDealerHand) > 21:
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("Draw 1")
    elif sum(cd.logicalPlayerHand) <= 21:
        if sum(cd.logicalDealerHand) > 21:
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("YOU WIN 1")
        elif sum(cd.logicalPlayerHand) > sum(cd.logicalDealerHand):
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("YOU WIN 2")
        elif sum(cd.logicalPlayerHand) < sum(cd.logicalDealerHand):
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("You lose 2")
        elif sum(cd.logicalPlayerHand) == sum(cd.logicalDealerHand):
            print(f"\nFinal hands:\n"
                  f"You:\n{cd.visualPlayerHand} total = {sum(cd.logicalPlayerHand)}\n"
                  f"Dealer:\n{cd.visualDealerHand} total = {sum(cd.logicalDealerHand)}\n")
            print("Draw 2 ")

    '''----------- PLAY AGAIN? -----------'''
    again = input("\nDo you want to play again? [Y] Yes [N] No\n").lower()
    if again == "y":
        # Cleaning the player hand
        cd.logicalPlayerHand.clear()
        cd.visualPlayerHand.clear()
        # Cleaning the Dealer hand
        cd.logicalDealerHand.clear()
        cd.visualDealerHand.clear()

        # Reset of the main deck
        cd.visualDeck = cd.deckBackup.copy()
    if again == "n":
        break
