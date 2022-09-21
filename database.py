# main imports

#from url import mongoUrl
#from pymongo import MongoClient
from resources.styles import styles
from time import sleep
from json import load, dumps
# colour constants

RESET=styles.RESET
FAILURE=styles.FAILURE

MONGODB_ENABLED=False

url=mongoUrl
myclient=MongoClient(url)

database=myclient["CasinoDatabase"]
members=database["CasinoMembers"]

def getRank(id):
	member=members.find_one({ "id": id })
	if member != None:
		rank=member["rank"] # current rank of the member in the database
		_id = member["_id"]
		
		if rank != "Administrator" and _id > 3 : 
			return "Member"
		elif _id <= 3 or member["money"] > 500000:
			members.update_one( { "rank": "Member" } , { "$set": { "rank": "Administrator" } } )
			return "Administrator"
	else:
		return "Member"

def getID(id):
	id_new=""
	if len(id) == 1: id_new=f"000{id}" # 3 zeros for 1 digit id
	if len(id) == 2: id_new=f"00{id}" # 2 zeros for 2 digit id
	if len(id) == 3: id_new=f"0{id}" # 1 zero for 3 digit id
	if len(id) == 4: id_new=f"{id}" # no zeros for 4 digit id
	if len(id) > 4 or len(id) < 1:
		print(FAILURE+"Invalid (id) Input"+RESET)
		return "INVALID"
	if id_new != "":
		if MONGODB_ENABLED != False:
			member=members.find_one({ "id": id_new})
			
			if member == None:
				name=input("Please state your name: ")
				if name.lower() == "end":
					from sys import exit
					exit(0)
				rankForData=getRank(id_new)
				id_count=members.count_documents({}) + 1
				data = { "_id": id_count, "id": id_new, "name": name.capitalize(), "money": 100, "rank": rankForData }	
				idQuery=members.insert_one(data)
				newMember=members.find_one({ "_id": idQuery.inserted_id })
				members.find().sort("_id", 1)
				return newMember
			else:
				getRank(id_new)
				return member
		else:
			member = open("./member.json", "r")
			return load(member)

def getMoneyFromId(member, id):
	#member=members.find_one({ "id": id}) # for when internet is used
	money=member["money"]
	return money

def giveMoney(member, increment):
	if MONGODB_ENABLED != False:
		print("MONGODB USED")
	else:
		money=member["money"]
		# rewrite to allow for mongodb and json saving
		if type(int(money)) == "int":
			return print(f"{FAILURE}Money is not a number{RESET}")
		if type(int(increment)) == "int":
			return print(f"{FAILURE}Increment is not a number{RESET}")
		file = open("./member.json", "w")
		data = dumps({ 
			"_id": member["_id"],
			"id": member[["id"]],
			"name": member["name"],
			"money": int(money) + int(increment),
			"rank": member["rank"]
		})
		file.write(data)

		return load(open("./member.json", "r"))["money"]

def takeMoney(member, decrement):
	money = member["money"]

	if type(int(money)) == "int":
		return print(f"{FAILURE}Money is not a number{RESET}")
	if type(int(decrement)) == "int":
		return print(f"{FAILURE}Increment is not a number{RESET}")
	file = open("./member.json", "w")
	data = dumps({
		"_id": member["_id"],
		"id": member[["id"]],
		"name": member["name"],
		"money": int(money) - int(decrement),
		"rank": member["rank"]
	})
	file.write(data)

	return load(open("./member.json", "r"))["money"]
