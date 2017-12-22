import pickle
class door:
	def __init__(self, name, dir, doorLocked = False):
		self.name = name
		self.doorLocked = doorLocked
		self.dir = dir
		
	def declareDes(self, description):
		self.description = description

class usables:
	def __init__(self, name, canTake = True, description = "Generic Description", item = None, result = None, hidden = False, customUse = None,use = None):
		self.name = name
		self.canTake = canTake
		self.description = description
		self.useSing = use
		self.useItem = item
		self.useResult = result
		self.hidden = hidden
		self.customUse = customUse
		self.useSing = None
		self.customSing = None
		
	def declareDes(self, description):
		self.description = description
		
	def declareUse(self, use, customSing = None):
		self.useSing = use
		self.customSing = customSing
		
	def declareCanUseWith(self, item, result, customUse = None):
		self.useItem = item
		self.useResult = result
		self.customUse = customUse
		
class room:
	def __init__(self, name, left = None, right = None, up = None, down = None, isLocked = False, description = "This is a generic description", obj = list()):
		self.name = name
		self.left = left
		self.right = right
		self.up = up
		self.down = down
		self.isLocked = isLocked
		self.description = description
		self.obj = obj
		
	def declareDes(self, description):
		self.description = description
		
	def declareObj(self, *objInRoom):
		self.obj = list(objInRoom)
		
def commandLook(room):
	notHidden = list();
	tempList = list()
	print(room.description)
	print("There is", end=" ");
	if(room.left != None):
		tempList.append(str("the \"" + room.left + "\" to the left"))
	if(room.right != None):
		tempList.append(str("the \"" + room.right + "\" to the right"))
	if(room.up != None):
		tempList.append(str("the \"" + room.up + "\" to the north"))
	if(room.down != None):
		tempList.append(str("the \"" + room.down + "\" to the south"))
	for i, c in enumerate(tempList):
		if(len(tempList) - i == 2):
			print(c + " and", end=" ")
		elif(len(tempList) - i == 1):
			print(c + ".")
		else:
			print(c + ",", end= " ")
			
	print("This room also has", end = " ")
	
	for i in room.obj:
		if(i.hidden == False):
			notHidden.append(i);
	if(notHidden):
		for i, c in enumerate(notHidden):
			if(len(notHidden) - i == 2):
				print("a \"" + c.name + "\" and", end=" ")
			elif(len(notHidden) - i == 1):
				print("a \"" + c.name + "\"", end=" ")
			else:
				print("a \"" + c.name + "\",", end= " ")
	else:
		print("nothing",end=" ")
		
	print("in here.")

def lookInv(playerInv):
	if(len(playerInv) >= 1):
		print("You have", end = " ")
		for i, c in enumerate(playerInv):
			if(len(playerInv) - i == 2):
				print("a \"" + c.name + "\" and", end=" ")
			elif(len(playerInv) - i == 1):
				print("a \"" + c.name + "\"", end=" ")
			else:
				print("a \"" + c.name + "\",", end= " ")
		print("in your inventory.")
	else:
		print("Your inventory is empty.")
	
def lookItem(playerInv, currentRoom, itemStr):
	itemFound = False
	for i in playerInv:
		if(i.name == itemStr):
			print(i.description)
			itemFound = True
			
	if (itemFound == False):	
		for c, i in enumerate(currentRoom.obj):
			if(i.name == itemStr and i.hidden == False):
				print(i.description)
				itemFound = True
			
	if(itemFound == False):
		print("You can not seem to find a " + itemStr + " around you.")
	
def helpCom(command):
	directCom = list(["up","down","left","right","west","east","north","west"])
	if(command == "move" or command == "goto"):
		print("move\\goto [destination]\n")
		print("Allows you to change the current room you are in by specifying the destination")
	elif(command == "help"):
		print("help [command]\n")
		print("Allows you to see information about a command")
	elif(command == "quit"):
		print("quit\n")
		print("Allows you to quit to the title screen.")
	elif(command in directCom):
		for c, i in enumerate(directCom):
			print(i, end="")
			if(c < len(directCom) - 1):
				print("\\",end="")
		
		print("\n\nAllows you to move in a certain direction.")
	elif(command == "use"):
		print("use [item1] [*item2]\n")
		print("Allows you to use an item or use two items together.")
	elif(command == "look"):
		print("look [*object]\n")
		print("Allows you to look at the room or an object more closely.")
	elif(command == "inv"):
		print("inv\n")
		print("Allows you to see what you have in your inventory.")
	elif(command == "pickup" or command == "take" or command == "get"):
		print("pickup\\get\\take [item]\n")
		print("Allows you to add an item to your inventory if you are able to.")
	elif(command == "me"):
		print("There are other services on Earth that can help you.")
	else:
		print("Command not recognized.")
	
def savToFile(savName,inv,loc,opDoor,takObj):
	savFile = open(str(savName) + ".csav", "wb")
	dataToStore = list([inv,loc,opDoor,takObj])
	pickle.dump(dataToStore, savFile)
	savFile.close()
	
def createSav():
	startInv = [0,0,0];
	startLoc = [0,0];
	startOpDoor = [0,0];
	startTakObj = [0,0,0];
	savName = str(input("What do you want to name the save?"));
	savToFile(savName,startInv,startLoc,startOpDoor,startTakObj)
	savFile = open(savName + '.csav','rb');
	readLine = pickle.load(savFile);
	print(readLine)
	print("Save file " + savName + " created.")
	savFile.close()
	bufferInput = input("press any key");
	savName = (savName + ".csav")
	return savName
	
def savDataToObj(savData,dataToCreate):
	for i in savData:
		for j in savData[i]:
			if (savData[i][j] == 1):
				dataToCreate[j]
	
def loadSav(savName):
	if savName == None:
		savName = input("What is the name of the save?\n>>>")
	savFile = open(savName, 'rb');
	savData = pickle.load(savFile)
	print("loaded")
	BLAH = input("continue")
	return savData
	
def initializeData():
	beginKey = usables("S_Key",True,hidden = False)
	beginKey.declareDes("It's a small silver key.")
	beginKey.declareCanUseWith("S_Lock",list(["unlock","Basement_Corridor"]))
	
	beginI1 = usables("Key's_Blade",True,hidden = False)
	beginI1.declareDes("It's a copper blade part of the key. It's not the other kind.")
	beginI1.declareCanUseWith("Key's_Bow",list(["combine","C_Key","inv"]),"You put the two pieces together to make a key.")
	
	beginI2 = usables("Key's_Bow",True,hidden = False)
	beginI2.declareDes("It's a copper handle part of the key.")
	beginI2.declareCanUseWith("Key's_Blade",list(["combine","C_Key","inv"]),"You put the two pieces together to make a key.")
	
	ballGem =  usables("Red_Gem",True, hidden = False)
	ballGem.declareDes("The gem glistens in your fist.")
	ballGem.declareCanUseWith("Skull_Bust",list(["unlock","Fire_Room"]))
	
	beginLock = usables("S_Lock", False, hidden = False)
	beginLock.declareDes("It's a silver lock.")
	beginLock.declareCanUseWith("S_Key",list(["unlock","Basement_Corridor"]))
	
	beginCLock = usables("C_Lock", False, hidden = False)
	beginCLock.declareDes("It's a coppper lock.")
	beginCLock.declareCanUseWith("C_Key",list(["unlock","Stairs"]))
	
	lockGold = usables("Gold_Lock", False, hidden = False)
	lockGold.declareDes("It's a golden lock.")
	
	lockSkull = usables("Skull_Bust",False,hidden = False)
	lockSkull.declareDes("It's a bust statue with a skull instead of a head. It has a red gem in one of it's eye sockets.")
	lockSkull.declareCanUseWith("Red_Gem",list(["unlock","Fire_Room"]),"You place the Red_Gem inside the Skull_Bust's eye.")
	
	itemOil = usables("Oil", True)
	itemOil.declareDes("It's a bottle of oil.")
	itemOil.declareCanUseWith("Rusty_Valve",list(["combine","Oiled_Valve","room"]))
	
	itemBucket = usables("Bucket",True)
	itemBucket.declareDes("It's a good sized bucket. It could probably hold a lot of things.")
	itemBucket.declareCanUseWith("Water",list(["combine","Water_Bucket","inv"]))
	
	propValveR = usables("Rusty_Valve",False)
	propValveR.declareDes("It's a rusty valve attached to some pipes.")
	propValveR.declareUse(list(["note","You cannot turn the valve because of how rusty it is."]))
	propValveR.declareCanUseWith("Oil",list(["combine","Oiled_Valve","room"]))
	
	propDesk = usables("Wooden_Desk",False)
	propDesk.declareDes("It's a nice shiny wooden desk.")
	
	propFire = usables("Fire_Pedestal",False)
	propFire.declareDes("It's a pedestal with a blinding ball of fire on top of it. The fire seems to be covering of something shiny.")
	propFire.declareCanUseWith("Water_Bucket",list(["combine","Golden_Key","room"]),"You threw the Water_Bucket at the Fire_Pedestal and knocked both of them into the fire below. Something flew out of the pedestal.")
	
	propPainting = usables("Painting",False)
	propPainting.declareDes("It's a a painting of a cat.")
	
	propToilet = usables("Toilet",False)
	propToilet.declareDes("It's a toilet. There's no water in the bowl for some reason.")
	propToilet.declareUse(list(["note","There does not seem to be any water to flush anything."]))
	
	propPipe = usables("Pipe",False)
	propPipe.declareDes("It's the pipe that leads to the toilet. It seems to be damaged beyond repair.")
	
	propHidden = usables("Hidden Prop",False, hidden = True)
	propHidden.declareDes("Hey, you're not suppose to see this!")
	
	beginRoom01 = room("Workshop", left = "Basement_Corridor")
	beginRoom01.declareDes("You are in a warm, cozy room with tools scattered atop a desk.")
	beginRoom01.declareObj(beginKey,beginLock,propDesk,beginI2,propHidden)
	
	beginRoom02 = room("Basement_Corridor",left="Water_Main",right = "Workshop", up = "Stairs", isLocked = True)
	beginRoom02.declareDes("You are in a cold corridor draped in a dim white light.")
	beginRoom02.declareObj(ballGem, beginCLock)
	
	beginRoom03 = room("Water_Main", right = "Basement_Corridor")
	beginRoom03.declareDes("You are in a room filled with pipes and gages.")
	beginRoom03.declareObj(propValveR,beginI1)
	
	transRoom01 = room("Stairs", up = "Purple_Room", down = "Basement_Corridor", isLocked = True)
	transRoom01.declareDes("The stairs appears to go on and on.")
	
	mainRoom01 = room("Purple_Room", left = "Red_Room", right = "Blue_Room", up = "Exit", down = "Stairs")
	mainRoom01.declareDes("The room envelops you in its floral purple wallpaper.")
	mainRoom01.declareObj(lockGold)
	
	mainRoom02 = room("Red_Room", down = "Restroom", left = "Fire_Room", right = "Purple_Room")
	mainRoom02.declareDes("The room radiates its fiery red wallpaper.")
	mainRoom02.declareObj(lockSkull,itemBucket)
	
	mainRoom03 = room("Blue_Room",down = "Restroom", left = "Purple_Room")
	mainRoom03.declareDes("The room oozes its cool blue aura around you.")
	mainRoom03.declareObj(itemOil)
	
	mainRoom04 = room("Restroom", left = "Red_Room", right = "Blue_Room")
	mainRoom04.declareDes("The bathroom is nice and clean. The floor is a nice, shiny marble tiling.")
	mainRoom04.declareObj(propPipe,propToilet)
	
	fireRoom = room("Fire_Room",right = "Red_Room", isLocked = True)
	fireRoom.declareDes("The room is a giant pit of fire. Good thing, you are on a platform above it.")
	fireRoom.declareObj(propFire)
	
	exitRoom = room("Exit", isLocked = True)
	exitRoom.declareDes("It's the exit.")
	
	roomList = ([beginRoom01,beginRoom02,beginRoom03,transRoom01,mainRoom01,mainRoom02,mainRoom03,mainRoom04,fireRoom,exitRoom])
	return roomList
	
def initItemLib():

	beginCombo =  usables("C_Key", False)
	beginCombo.declareDes("It's a copper key.")
	beginCombo.declareCanUseWith("C_Lock",list(["unlock","Stairs"]))

	itemWater = usables("Water",False)
	itemWater.declareDes("It's puddle of water. You can probably scoop all of it up.")
	itemWater.declareCanUseWith("Bucket",list(["combine","Water_Bucket","inv"]))
	
	comboWBucket = usables("Water_Bucket",True)
	comboWBucket.declareDes("The bucket is filled with a bit of water")
	comboWBucket.declareCanUseWith("Fire_Pedestal",list(["combine","Golden_Key","room"]),"You threw the Water_Bucket at the Fire_Pedestal and knocked both of them into the fire below. Something flew out of the pedestal.")
	
	goldKey = usables("Golden_Key",True)
	goldKey.declareDes("Wow, it's a golden key! So shiny!")
	goldKey.declareCanUseWith("Gold_Lock",list(["unlock","Exit"]))
	
	propValveO = usables("Oiled_Valve",False)
	propValveO.declareDes("Wow! It's so slippery.")
	propValveO.declareUse(list(["create","Water","Restroom"]),"You hear a short gush of water above you.")
	
	itemLib = ([beginCombo,goldKey, comboWBucket,propValveO, itemWater])
	return itemLib
	

def openDoor(door,usables):
	if (usables.useWithItem == door.name):
		door.doorLocked = False
		
	else:
		print("Not the right door...")
	
def checkRoomExists(room, destination):
	exists = False
	if(room.left == destination):
		exists = True
	if(room.right == destination):
		exists = True
	if(room.up == destination):
		exists = True
	if(room.down == destination):
		exists = True
	return exists
	
def exitGame():
	print("Game ended.")
	return True
	

def commandToWoLi():
	#turns user's input into a list of words
	playerCom = list()
	befCount = 0;
	x = 0
	choice = input("\n>>>") + " ";
	for i, c in enumerate(choice):
		if (x < 5):
			if (c == " "):
				playerCom.append(choice[befCount:i]);
				befCount = i+1;
				x += 1
	while(x < 5):
		playerCom.append(None)
		x += 1
		
	#print(playerCom)
	return playerCom
	
def changeRoom(roomName, roomArray, currentRoom):
	tempRoom = None
	for i, c in enumerate(roomArray):
		if(roomArray[i].name == currentRoom.name):
			roomArray.remove(c)
			roomArray.append(currentRoom)
		
		if(roomArray[i].name == roomName):
			if((roomArray[i].isLocked) == False):
				tempRoom = roomArray[i]
				
			elif(roomArray[i].isLocked):
				print("The path to the \"" + roomArray[i].name + "\" is locked.")
				tempRoom = currentRoom
				
	if(tempRoom == None):			
		print("Room does not exists.")
		tempRoom = currentRoom
	
	return tempRoom
	
def unlockRoom(roomName, roomArray):
	for i, c in enumerate(roomArray):
		if(roomArray[i].name == roomName):
			if((roomArray[i].isLocked)):
				print("\"" + roomArray[i].name + "\" is now unlocked.")
				roomArray[i].isLocked = False;
				
			elif((roomArray[i].isLocked) == False):
				print("\"" + roomArray[i].name + "\" is already unlocked.")
	
def useItem(use1, currentRoom, roomArray, playerInv, itemLib):
	resultList = list()
	item1 = None
	item1Info = list()
	item1Index = None
	item2 =  None
	item2Info = list()
	item2Index =  None
	
	for i in playerInv:
		if(i.name == use1 and item1 == None):
			item1 = i
			item1Info = "pI"
			
	for c, i in enumerate(currentRoom.obj):
		if(i.name == use1 and i.hidden == False and item1 == None):
			item1 = i
			item1Info = "cR"
			item1Index = c
			
	if(item1):
		if(item1.useSing != None):
			resultList = item1.useSing
			if(resultList[0] == "create"):
				for i in itemLib:
					if(resultList[1] == i.name):
						item2 = i
				if(resultList[2] == currentRoom.name):
					currentRoom.obj.append(item2)
				else:
					for c, i in enumerate(roomArray):
						if(i.name == resultList[2]):
							roomArray[c].obj.append(item2)
				if(item1Info == "cR"):
					currentRoom.obj[item1Index].useSing[0] = "used"
				if(item1.customSing != None):
					print(item1.customSing)
				else:
					print("You have used " + item1.name)
					
			elif(resultList[0] == "note"):
				print(resultList[1])
				
			elif(resultList[0] == "used"):
				print("You have already used this thing.")
			else:
				print("You cannot use the " + item1.name + "?")
				
		else:
			print("You cannot use the " + item1.name + ".")
		
	else:
		print("You cannot use " + use1 + " because it does not exists.")
	
	
def useItems(use1, use2, currentRoom, roomArray, playerInv, itemLib):
	resultList = list()
	item1 = None
	item1Info = list()
	item1Index = None
	item2 =  None
	item2Info = list()
	item2Index =  None
	item3 = None
	
	for i in playerInv:
		if(i.name == use1 and item1 == None):
			item1 = i
			item1Info = "pI"
			#print(item1.name + "1")
		if(i.name == use2 and item2 == None):
			item2 = i
			item2Info = "pI"
			#print(item2.name + "2")
			
	for c, i in enumerate(currentRoom.obj):
		if(i.name == use1 and i.hidden == False and item1 == None):
			item1 = i
			item1Info = "cR"
			item1Index = c
			#print(item1.name + "3")
		if(i.name == use2 and i.hidden == False and item2 == None):
			item2 = i
			item2Info = "cR"
			item2Index = c
			#print(item2.name + "4")
	if(item1 != None and item2 != None):	
		#print(item1.name + " " + item2.name)
		
		
		if(item1.useItem == item2.name):
			resultList = item1.useResult	
			if(resultList[0] == "unlock"):
				if(item1.customUse != None):
					print(item1.customUse)
				else:
					print("You have used the " + item1.name + " to unlock the " + item2.name + ".")
				unlockRoom(resultList[1],roomArray)
			elif(resultList[0] == "combine"):
				for i in itemLib:
					if(resultList[1] == i.name):
						item3 = i
						
				if(resultList[2] == "inv"):
					playerInv.append(item3)
				elif(resultList[2] == "room"):
					currentRoom.obj.append(item3)
					
				if(item1Info =="pI"):
					playerInv.remove(item1)
				elif(item1Info == "cR"):
					currentRoom.obj[item1Index].canTake = False
					currentRoom.obj[item1Index].hidden = True
				if(item2Info =="pI"):
					playerInv.remove(item2)
				elif(item2Info == "cR"):
					currentRoom.obj[item2Index].canTake = False
					currentRoom.obj[item2Index].hidden = True
				
				if(item1.customUse != None):
					print(item1.customUse)
				else:
					print("You have used the " + item1.name + " and " + item2.name + " to make the " + item3.name + ".")
		else:
			print(use1 + " and " + use2 + " cannot be used together.")
	elif(item1):
		print(use2 + " cannot be used because it does not exists.")
		
	elif(item2):
		print(use1 + " cannot be used because it does not exists.")
	else:
		print("Neither items exists, so they cannot be used.")
				
	
def pickupItem(item, playerInv, currentRoom, roomArray):
	roomIndex = None
	itemToStore = None
	runAllIt = False
	cannotPick = False
	
	for i in currentRoom.obj:
		if((item == i.name) and i.canTake == True):
			playerInv.append(i)
			i.canTake = False
			i.hidden = True
			runAllIt = True
		elif((item == i.name) and i.canTake == False):
			cannotPick = True
	
	if(runAllIt):
		for i, c in enumerate(roomArray):
			if(c.name == currentRoom.name):
				roomIndex = i		
			
		roomArray[roomIndex] = currentRoom
		print("You picked up a " + item + ".")
		
	elif(cannotPick):
		print("You can not pick up the " + item + ".")
		
	else:
		print(item + " does not exist.")
		
def combineItem(item1, item2, currentRoom, playerInv):
	pass
	
	
	
def checkIfDir(command):
	isDir = False
	dirList = list(["left","right","up","down","west","east","north","south"])
	for i in dirList:
		if(command == i):
			isDir = True
	return isDir

	
def mainState():
	activeState = True
	playerCom = list()
	playerInv = list()
	roomExitExists = False
	secondIsDir = False
	hasMoved = False
	winRoom = "Exit"
	roomArray = initializeData()
	currentRoom = roomArray[0]
	itemComLibrary = initItemLib()
	
	while(activeState == True):
		print("\nYou are in the \"" + currentRoom.name + "\".\n")
		commandLook(currentRoom)
		
		if(currentRoom.name == winRoom):
			creditsState()
			activeState = False
			
		playerCom = commandToWoLi()
		print("\n")
		
		roomExitExists = False
		secondIsDir = False
		hasMoved = False
		if (activeState):
			if(playerCom[0] == "move" or playerCom[0] == "goto"):
				roomExitExists = checkRoomExists(currentRoom, playerCom[1])
				secondIsDir = checkIfDir(playerCom[1])
					
				if(roomExitExists):
					currentRoom = changeRoom(playerCom[1], roomArray, currentRoom)
					hasMoved = True
						
				elif(secondIsDir):
					playerCom[0] = playerCom[1]
						
			if(playerCom[0] == "left" or playerCom[0] == "west"):
				if(currentRoom.left != None):
					currentRoom = changeRoom(currentRoom.left, roomArray, currentRoom)
					hasMoved = True
							
			elif(playerCom[0] == "right" or playerCom[0] == "east"):
				if(currentRoom.right != None):
					currentRoom = changeRoom(currentRoom.right, roomArray, currentRoom)
					hasMoved = True
				
			elif(playerCom[0] == "up" or playerCom[0] == "north"):
				if(currentRoom.up != None):
					currentRoom = changeRoom(currentRoom.up, roomArray, currentRoom)
					hasMoved = True
							
			elif(playerCom[0] == "down" or playerCom[0] == "south"):
				if(currentRoom.down != None):
					currentRoom = changeRoom(currentRoom.down, roomArray, currentRoom)
					hasMoved = True
						
			if(hasMoved == False and (checkIfDir(playerCom[0]) or playerCom[0] == "move")):
				print("You hit a wall!")
				hasMoved = True
			
			if(hasMoved == False):
				if(playerCom[0] == "use"):
					if(playerCom[1] != None and playerCom[2] != None and playerCom[3] == None):
						useItems(playerCom[1], playerCom[2], currentRoom, roomArray, playerInv,itemComLibrary)
					if(playerCom[1] != None and playerCom[2] == None):
						useItem(playerCom[1], currentRoom, roomArray, playerInv,itemComLibrary)
					if(playerCom[1] == None):
						print("Use what?")
				
				elif(playerCom[0] == "pickup" or playerCom[0] == "get" or playerCom[0] == "take"):
					if(playerCom[1] != None):
						pickupItem(playerCom[1], playerInv, currentRoom, roomArray)
					else:
						print("Get what?")
				
				elif(playerCom[0] == "look"):
					if(playerCom[1] == "room" or playerCom[1] == None):
						commandLook(currentRoom)
					elif(playerCom[1] == "inv" or playerCom[1] == "inventory"):
						lookInv(playerInv)
					else:
						lookItem(playerInv,currentRoom,playerCom[1])
				
				#elif(playerCom[0] == "unlock"):
				#	roomExitExists = checkRoomExists(currentRoom, playerCom[1])
				#	unlockRoom(playerCom[1], roomArray)
				
				elif(playerCom[0] == "inv"):
					lookInv(playerInv)
				
				elif(playerCom[0] == "help"):
					if(playerCom[1] != None):
						helpCom(playerCom[1])
					else:
						print("Avaliable commands: " + "move, left, right, up, down, get, take, pickup, goto, look, inv, use, help, quit.\n")
						print("Type \"help\" and a command like \"help move\" to see more details. \"\\\" indicates an alternative or similar command that can be used in its place. * means the argument is optional.")
				
				elif(playerCom[0] == "quit"):
					activeState = False
					
				elif(playerCom[0] == "awoo" or playerCom[0] == "awoo~"):
					print("awoo~")
					
				else:
					print("Invalid Command\n")
			
def creditsState():
	print("Congratulations, you have reached the exit of this house!\n")
	print("I hope you enjoyed this short game. Goodbye for now.\n")
	print("Made by CoalVoltage in Python\nType anything to continue.\n")
	
def main():
	quitGame = False
	activeGame = False
	nameOfGame = "Crummy Room Text Adventure"
	while(quitGame == False):
		print("\nWelcome to " + nameOfGame + " made by CoalVoltage.\n\n1. Start the game. \"begin\" \n2. Exit game. \"quit\"\n\nFor help, type \"help\"\n")
		
		introAct = commandToWoLi();
		print(end="\n")
		
		if (introAct[0] == "begin"):
			mainState()
			
		elif (introAct[0] == "quit"):
			quitGame = exitGame();
			
		elif (introAct[0] == "help"):
			if(introAct[1] != None):
				helpCom(introAct[1])
			else:
				print("\nAvaliable commands: " + "move, left, right, up, down, goto, take, get, pickup, look, inv, use, help, quit.\n")
				print("Type \"help\" and a command like \"help move\" to see more details. \"\\\" indicates an alternative or similar command that can be used in its place. * means the argument is optional.")
		else:
			print("\nInvalid command")

if __name__ == "__main__":
	main()
	
	
	