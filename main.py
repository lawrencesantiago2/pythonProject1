import random
class Card: #Class for Card (OOP)
    def __init__(self, num, sym):
        self.cardNum = num
        self.cardSym = sym

cardNumList =[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        #List of card numbers
cardSymList = [' Clover', ' Spade', ' Hearts', ' Diamond']
        #List of Card symbols
cardDict = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

def cardStraightChecker(hand, pokerRiver):
    list = []
    straightCounter = 0
    for x in range(0, 2):
        list.append(hand[x].cardNum)
    for x in range(0, 5):
        list.append(pokerRiver[x].cardNum)
    list.sort()
    for x in range(0,6):
        if list[x] <= list[x] + 1 and list[x+1] == list[x] + 1:
            straightCounter += 1
        else:
            straightCounter -= 1
    return straightCounter


def cardSuitChecker(hand, pokerRiver):
    suitCounter = 0
    for x in range(0, 2):
        for y in range(0, 5):
            if hand[x].cardSym == pokerRiver[y].cardSym:
                suitCounter += 1
            else:
                suitCounter -= 1
    return suitCounter
            # Check for flush

def cardPairChecker(card, pokerRiver):
    pairCounter = 0
    for y in range(0, 5):
        if card.cardNum == pokerRiver[y].cardNum:
            pairCounter += 1
    return pairCounter
            # Check for pairs,3 of a kind, 4 of a kind, and full house

def scorer(playerHand, pokerRiver, value1, value2):
    if cardStraightChecker(playerHand, pokerRiver) >= 5 and cardSuitChecker(playerHand, pokerRiver) >= 5:
        print("Straight Flush")
        return 90
    elif cardStraightChecker(playerHand, pokerRiver) >= 5:
        print("Straight")
        return 50   #
    elif cardSuitChecker(playerHand, pokerRiver) >= 5:
        print("Flush")
        return 60   #
    elif playerHand[0].cardNum == playerHand[1].cardNum and value1 == 1 and value2 == 1:
        print("3 of a kind")
        return 40   #
    elif playerHand[0].cardNum == playerHand[1].cardNum:
        print("Pair")
        return 20   #
    elif value1 == 1 and value2 == 1:
        print("2 Pairs")
        return 40   #
    elif value1 == 1 or value2 == 1:
        print("Pair")
        return 20   #
    elif value1 == 2 and value2 == 1:
        print("Full House!")
        return 70 #
    elif value1 == 1 and value2 == 2:
        print("Full House!")
        return 70 #
    elif value1 == 2 or value2 == 2:
        print("3 of a kind")
        return 40 #
    elif value1 == 3 or value2 == 3:
        print("4 of a kind")
        return 80 #
    else:
        print("High card")
        return 0
            # Checker for score of hand
def cardKicker(playerHand, computerHand):
    list1 = []
    list2 = []
    for x in range(0, 2):
        list1.append(playerHand[x].cardNum)
        list2.append(computerHand[x].cardNum)
    list1.sort()
    print(list1)
    list2.sort()
    print(list2)
    if list1[1] == list2[1]:
        if cardSymList.index(playerHand[0].cardSym) > cardSymList.index(computerHand[0].cardSym) and cardSymList.index(playerHand[0].cardSym) > cardSymList.index(computerHand[1].cardSym):
            return True
        elif cardSymList.index(playerHand[1].cardSym) > cardSymList.index(computerHand[0].cardSym) and cardSymList.index(playerHand[1].cardSym) > cardSymList.index(computerHand[1].cardSym):
            return True
        else:
            return False
    elif list1[1] > list2[1]:
        return True
    else:
        return False
            # Check who has the higher card

def createDeck(cardNumList, cardSymList):
    list = []
    for x in range(0, 4):
        for y in range(0, 13):
            card = Card(cardNumList[y], cardSymList[x])
            list.append(card)
    return list
            # Create the deck

def createRiver(cardDeck):
    list = []
    for x in range(0, 5):
       list.append(cardDeck.pop(random.randint(0, len(cardDeck)-1)))
    return list
            # Create the river

def createHand(deck):  #Create players hand
    list = []
    for x in range (0,2):
        list.append(deck.pop(random.randint(0,len(deck)-1)))
    return list




#Main
cardDeck = createDeck(cardNumList, cardSymList)
pokerRiver = createRiver(cardDeck)
playerHand = createHand(cardDeck)
computerHand = createHand(cardDeck)
print("Poker River: ")
for x in range(0, 5):
    if pokerRiver[x].cardNum > 10:
        print(cardDict[pokerRiver[x].cardNum] + pokerRiver[x].cardSym)
    else:
        print(str(pokerRiver[x].cardNum) + pokerRiver[x].cardSym)

print("Player Hand: ")
for x in range(0, 2):
    if playerHand[x].cardNum > 10:
        print(cardDict[playerHand[x].cardNum] + playerHand[x].cardSym)
    else:
        print(str(playerHand[x].cardNum) + playerHand[x].cardSym)
print("Computer Hand: ")
for x in range(0, 2):
    if computerHand[x].cardNum > 10:
        print(cardDict[computerHand[x].cardNum] + computerHand[x].cardSym)
    else:
        print(str(computerHand[x].cardNum) + computerHand[x].cardSym)
print("Player's hand value")
playerScore = scorer(playerHand, pokerRiver, cardPairChecker(playerHand[0], pokerRiver), cardPairChecker(playerHand[1], pokerRiver))
print("Computer's hand value")
computerScore = scorer(computerHand, pokerRiver, cardPairChecker(computerHand[0], pokerRiver), cardPairChecker(computerHand[1], pokerRiver))

if playerScore == computerScore:
    if cardKicker(playerHand, computerHand):
        print("You win")
    else:
        print("You lose")
elif playerScore > computerScore:
    print("You win")
else:
    print("you lose")




















