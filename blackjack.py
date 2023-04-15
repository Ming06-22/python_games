import random, sys

HEART, DIAMONDS, SPADES, CLUBS = chr(9829), chr(9830), chr(9824), chr(9827)
BACKSIDE = "backside"

def main():
    print("Rules: Try to get as close to 21 without going over.\n       King, Queens, and Jacks are worth 10 points.\n\
       Aces are worth 1 or 11 points.\n       Cards2 through 10 are worth their face value.\n       (H)it to take another card.\n\
       (S)tand to stop taking cards.\n       On your first play, you can (D)ouble down to increase your bet\n\
       but must hit exactly one more time before standing.\n       In case of a tie, the bet is returned to the player.\n\
       The dealer stopshitting at 17.")
    
    money = 5000
    while (True):
        # check whether the player still have money
        if (money <= 0):
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()
            
        # ask player to enter this round's bet
        print(f"Money: {money}")
        bet = getBet(money)
        
        # give cards to player and dealer
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        
        print(f"Bet: {bet}")
        while (True):
            # display player's and dealer's cards
            displayHands(playerHand, dealerHand, False)
            print("")
            
            # check whether the points are over 21
            if (getHandValue(playerHand) > 21):
                break
            
            # ask for next movement
            move = getMove(playerHand, money - bet)
            if (move == "D"):
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f"Bet increased to {bet}.")
                print(f"Bet: {bet}")
                
            if (move in ("H", "D")):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}.")
                playerHand.append(newCard)
                
                if (getHandValue(playerHand) > 21):
                    continue
                
            if (move in ("S", "D")):
                break
            
            if (getHandValue(playerHand) <= 21):
                while (getHandValue(dealerHand) < 17):
                    print("Dealer hits...")
                    dealerHand.append(deck.pop())
                    displayHands(playerHand, dealerHand, False)
                    
                    if (getHandValue(dealerHand) > 21):
                        break
                    
                    input("Press Enter to continue...")
                    print("\n\n")
                    
            displayHands(playerHand, dealerHand, True)
            
            # decide who to win
            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
            if (dealerValue > 21):
                print(f"Dealer busts! You win {bet}!")
                money += bet
            elif (playerValue > 21 or playerValue < dealerValue):
                print("You lost!")
                money -= bet
            elif (playerValue > dealerValue):
                print(f"You won {bet}")
                money += bet
            elif (playerValue == dealerValue):
                print("It's a tie, the bet is turned to you.")
                
            input("Press Enter to continue...")
            print("\n\n")
            
# ask entering the bet
def getBet(maxBet):
    while (True):
        print(f"How much do you bet?(1-{maxBet}, or QUIT)")
        bet = input("> ").upper().strip()
        if (bet == "QUIT"):
            print("Thanks for playing")
            sys.exit()
        if (not bet.isdecimal()):
            continue
        bet = int(bet)
        if (1 <= bet <= maxBet):
            return bet
        
# shuffle the card
def getDeck():
    deck = []
    for suit in (HEART, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    
    return deck

# display player's cards and dealer's cards
def displayHands(playerHand, dealerHand, showDealerHand):
    print("")
    if (showDealerHand):
        print(f"DEALER: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        displayCards([BACKSIDE] + dealerHand[1: ])
        
    print(f"PLAYER: {getHandValue(playerHand)}")
    displayCards(playerHand)
    
# get the sum of cards
def getHandValue(cards):
    value, numberOfAces = 0, 0
    
    for card in cards:
        rank = card[0]
        if (rank == "A"):
            numberOfAces += 1
        elif (rank in ("J", "Q", "K")):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if (value + 10 <= 21):
            value += 10
            
    return value

# dispaly card
def displayCards(cards):
    rows = ["", "", "", "", ""]
    
    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if (card == BACKSIDE):
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "

    for row in rows:
        print(row)

# ask to enter the next movement
def getMove(playerHand, money):
    while (True):
        moves = ["(H)it", "(S)tand"]
        
        if (len(playerHand) == 2 and money > 0):
            moves.append("(D)ouble down")
        
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if (move in ("H", "S") or (move == "D" and "(D)ouble down" in moves)):
            return move
        
if (__name__ == "__main__"):
    main()