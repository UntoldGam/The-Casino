from database import getID, getMoneyFromId
from resources.styles import styles
from resources.functions import clear, gameChoice

# COLOUR CONSTANTS


RESET = styles.RESET
BLUE = styles.BLUE
SUCCESS = styles.SUCCESS
LIGHT_BLUE = styles.LIGHT_BLUE
BLUETEXT = styles.BLUETEXT
UNDERLINE = styles.UNDERLINE

# DEBUG / TESTING CONSTANTS

# bypasses certain inputs that are not essential to the Casino Games or Casino Login
dev_bypass = True

# MAIN CODE (handles login and game selection) (mostly backend)


def begin():
	# FIX TO MAKE ONLY THE FIRST PRINT BLUE
	# add blue+ to the start of the print below to make all text blue (fix)
	print("Welcome to the Casino!")

	# id=input("Please state your player id: ")
	# if id.lower() == "end":
	#	from sys import exit
	#	exit(0)
	id="1"  # testing purposes
	member= getID(id)
	if member != "INVALID":
		member_name = member["name"]
		member_id = member["id"]
		member_rank = member["rank"]
		print(SUCCESS+"You have been logged in successfully"+RESET)

		print(f"Welcome to The Casino {member_name.capitalize()}")
		print(f"Your id is {UNDERLINE+member_id+RESET}")
		if member_rank == "Administrator":
			print(f"Your Rank is {BLUETEXT+member_rank+RESET}\n")
		else:
			print(f"Your Rank is {LIGHT_BLUE+member_rank+RESET}\n")
		money = getMoneyFromId(member, member_id)
		return member, money
	else:
		return "INVALID", "INVALID"




member, money = begin()
if member != "INVALID" and money != "INVALID":
    gameChoice(member, money)
