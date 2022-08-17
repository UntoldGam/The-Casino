from database import giveMoney, takeMoney
from random import randrange, shuffle
from sys import exit
from resources.functions import clear, gameChoice

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
cardNames = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
						7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Ace"}

hand = {"human": [], "casino": []}

deck = []
goalDeck = []

class Card:

	def __init__(self, rank):
		self.rank = rank

	def __str__(self):
		return (f"{cardNames[self.rank]} ({self.rank})")

	def cardValue(self):
		return (self.rank)

	def cardName(self):
		return (cardNames[self.rank])


def goalCount():
	# shuffles the deck of cards
	shuffle(deck) 
	shuffle(deck)
	shuffle(deck)  
	# adds 2 cards from the deck to the goal deck
	goalDeck.append(deck.pop(0))
	goalDeck.append(deck.pop(0))
	# adds up the value of the 2 cards in the goal deck
	count = 0
	for card in goalDeck:
		count += card.cardValue()
		print(card)
	return count # returns the value of the goal deck 

def starterBet(money, devBypass):
	if devBypass == True:
		bet = money / 2
	else:
		bet = 0
		while bet == 0:
			betInput = int(input("How much money do you wish to bet? "))
			if betInput > (money - 10):
				print("The bet you entered is higher than your balance - 10")
				continue
			else:
				print(f"The bet starts at £{betInput}")
				print("\n")
				bet = betInput
				break
		return bet


def showHand(hand, player):
	if player != "casino":
			print("Your hand: ")
	else:
			print("The Casino's Hand: ")
	for card in hand:
			print(f"{card}),")


def showGoal():
	count = 0
	for card in goalDeck:
		count += card.cardValue()
	print(f"GOAL: {count}")


def countHand(hand):
	count = 0
	for card in hand:
			count += card.cardValue()
	return count


def handCheck(hand, goal):
	handCount = countHand(hand)
	if handCount == goal or handCount + 1 == goal or handCount - 1 == goal:
		return True
	else:
		return False


def starterCards():
	hand["human"].append(deck.pop(0))
	hand["casino"].append(deck.pop(0))
	showGoal()
	showHand(hand["human"], "human")
	print("\n")
	showHand(hand["casino"], "casino")


def endGame(winner, member, bet, dev_bypass):
	clear()
	cont = False
	print(f"\nGame Over. \nThe winner is {winner}!")

	deck.extend(hand["casino"])
	deck.extend(hand["human"])

	del hand["casino"][:]
	del hand["human"][:]
	deck.clear()

	again = input("Do you wish to play again? (Y)es or (N)o? ").lower()
	if again == 'n':
		if winner == "You":
			print(f"£{giveMoney(member, bet)}")
		else:
			print(f"£{takeMoney(member, bet)}")
		gameChoice(member, member["money"], dev_bypass)
	elif again == 'y':
		cont = True
	return cont


def higherorlower(member, devBypass):
	for rank in range(len(deck) * 4):  # 1 -> 12 (11)
		deck.append(Card(rank))
		print(rank)
	playing = True
	name = member["name"]
	money = member["money"]
	print(f"\nWelcome {name} to Higher or Lower \nThe aim of the game is simple: you're given a card, if that card's value is within 1 number of the Computer's chosen number then you win, if it isn't, you lose.\n\nYou can either: Hit (take another card), Double (double the bet and cannot take anymore cards, only the card given on this move), Stand (take 0 cards) or Quit (end the game)\n")

	bet = starterBet(money, devBypass)
	goal = goalCount()
	starterCards()
	while playing == True:
			CasinoBust = False
			HumanBust = False
			HumanTurn = True
			CasinoTurn = False

			
			if handCheck(hand["human"], goal) == True:
					endGame("You", member, bet, devBypass)
			else:
					print("\n")
					actionInput = input("Do you wish to (H)it, (D)ouble, (S)tand or (Q)uit? ").lower()
					if actionInput == "h":
						hand["human"].append(deck.pop(0))
						showHand(hand["human"],"human")
						print("\n")
						showHand(hand["casino"], "casino")
						if handCheck(hand["human"], goal) == True:
								HumanTurn == False
								CasinoTurn = False
								cont = endGame("You", member, bet, devBypass)
								if cont == True:
									playing = True
						else:
								HumanTurn = False
								CasinoTurn = True

			if handCheck(hand["casino"], goal) == True:
				endGame("The Casino", member, bet, devBypass)
			else:
				hand["casino"].append(deck.pop(0))

				showHand(hand["human"],"human")
				print("\n")
				showHand(hand["casino"], "casino")
				if handCheck(hand["casino"], goal) == True:
						HumanTurn == False
						CasinoTurn = False
						cont = endGame("The Casino", member, bet, devBypass)
						if cont == True:
							playing = True
				else:
						HumanTurn = True
						CasinoTurn = False
