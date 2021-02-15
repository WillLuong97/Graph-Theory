#Problem 841. Keys and Rooms

'''
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
'''
from collections import defaultdict
def canVisitAllRooms(rooms):
	#building out the graph reprensentation of the rooms
	roomsGraph = defaultdict(list)
	#getting the room number of each room
	for room in range(len(rooms)):
		#getting the key from each room
		for key in rooms[room]:
			if roomsGraph[room]: 
				roomsGraph[room].append(key)
			else:
				roomsGraph[room] = [key]
	
	unlocked = [False] * len(rooms)
	#helper method to run dfs through the graph
	def dfs(room):
		#unlocking the current room
		unlocked[room] = True 
		#getting the key in the current room to unlock the next room
		for key in roomsGraph[room]:
			if not unlocked[key]:
				dfs(key) 
			

	#we all start with room 0, because it is always unlocked
	dfs(0)
	return all(unlocked)

def canVisitAllRooms_ITERATIVELY(rooms):
	#array to store all the unlocked room:
	unlocked = [False] * len(rooms)
	unlocked[0] = True
	stack = [0]
	while stack:
		room = stack.pop()
		for key in rooms[room]:
			if not unlocked[key]:
				unlocked[key] = True
				stack.append(key) 	
	return all(unlocked)

#Main function to run the test cases:
def main():
	print("TESTING KEYS AND ROOM...")
	#Test cases: 
	rooms =[[1],[2],[3],[]]
	print(canVisitAllRooms_ITERATIVELY(rooms))
	rooms = [[1,3],[3,0,1],[2],[0]]	
	print(canVisitAllRooms_ITERATIVELY(rooms))
	print("END OF TESTING...")

main()
