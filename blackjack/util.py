import cards_deck as cd
import random


# Shuffle the visualDeck
def shuffle():
    random.shuffle(cd.visualDeck)
    return cd.visualDeck


# Push a card from deck, and add to the visual hand of player or dealer.
def push(who):
    if who == "player":
        take_card = cd.visualDeck[0]

        cd.visualDeck.remove(take_card)
        cd.visualPlayerHand.append(take_card)

        cd.logicalPlayerHand.append(logic_hand(take_card))
        # print(cd.logicalPlayerHand)
        return take_card
    else:
        take_card = cd.visualDeck[0]

        cd.visualDeck.remove(take_card)
        cd.visualDealerHand.append(take_card)

        cd.logicalDealerHand.append(logic_hand(take_card))
        return take_card


# Change the string values to integer values
def logic_hand(card):
    if card in ["A♥️", "A♣️", "A♦️", "A♠️",
                "2♥️", "2♣️", "2♦️", "2♠️",
                "3♥️", "3♣️", "3♦️", "3♠️",
                "4♥️", "4♣️", "4♦️", "4♠️",
                "5♥️", "5♣️", "5♦️", "5♠️",
                "6♥️", "6♣️", "6♦️", "6♠️",
                "7♥️", "7♣️", "7♦️", "7♠️",
                "8♥️", "8♣️", "8♦️", "8♠️",
                "9♥️", "9♣️", "9♦️", "9♠️"]:
        if card in ["A♥️", "A♣️", "A♦️", "A♠️"]:
            return 1
        else:
            return int(card[0])
    elif card in ["10♥️", "10♣️", "10♦️", "10♠️",
                  "Q♥️", "Q♣️", "Q♦️", "Q♠️",
                  "J♥️", "J♣️", "J♦️", "J♠️",
                  "K♥️", "K♣️", "K♦️", "K♠️"]:
        return 10
