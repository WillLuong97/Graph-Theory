#Problem 959. Regions Cut By Slashes


'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.
Example 1:
Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\ , or ' '.

'''

'''

Observation:
 
Grid is a 2x2 array of string values; and the length of each string represent how many 1x1 squares are in line. 
The value contains in each string is a slash and it can be used to divide the grid into regions
Any diagonal slashses of the same kind can be morphed into bigger slash and divide a larger region of the grid. 

Requirements:
1. loop through each string and keep track of the slashes and its type, whether it is "/" or "\\"
2. Check if any slashse can be morphed into a biggger slash and can divide a bigger region
3. Divide the region based on the slash type and count the regions.



Approach: Breadth first search: 
'''
def regionsBySlashes(grid):
	#base case: 
	if not grid: 
		return 0 
	#creating a garph from the representation by adding 4 triangle
	#to represent as the graph node
	R = len(grid)
	C = len(grid[0])
	#a queue data structure to store the graph node
	allSection = set()
	#graph node that can be slashed by the \\ slash
	dir1 = [1, 0, 3, 2]
	#graph node that can be slashed by the  / slash
	dir2 = [3,2,1,0] 
	
	#loop through the matrix and start slashing and counting the region
	for i in range(R):
		for j in range(C):
			for k in range(4):
				#append the coordinate and graph node onto the queue
				allSection.add((i,j,k))
	#helper method to find all conected graph node and count the number of regions from there
	def findConnectedComponents(square):
		#getting the row and column:
		i = square[0]
		j = square[1]

		#checking for the slashes: 
		#return the region after getting slashed by \\
		if grid[square[0]][square[1]]== "\\":
			yield (i, j, dir1[square[2]])
			if square[2] <= 1: 
				if i - 1 >= 0:
					yield (i-1, j, 2)
				if j+1 < C:
					yield (i, j+1, 3)	
		#return the region slashed by /	
		else if grid[square[0]][square[1]] == "/":
			yield (i, j, dir2[square[2]])

		#otherwise, no slashes return all connected graph node
		else: 
			for node in range(4):
				if node != 2: 
					yield (i, j+1, node)
			yield (i-1, j, 2)
			yield (i+1, j, 0)
			yield (i, j-1, 1)
			yield (i, j+1, 3)
			
	
	result = 0 
	#checking all possible section with graph node and pass them into the 
	#bfs function and it will return back how many actual component are still connected after 
	#slashes
	while(len(allSection) > 0):
		start = []
		#pop the element out from the queue
		#put these element into a seperate array so that we can start running bfs
		start.append(allSection.pop())
		while start: 
			current_square = start.pop(0)
			allSection.discard(current_square)
			for neighbor in findConnectedComponents(current_square):
				if neighbor in allSection:
					allSection.discard(neighbor) 
					start.append(neighbor)

		result += 1	
	
	return result
					
#Main function to run the test cases: 
def main():
	print("TESTING REGIONS CUT BY SLASHES...")
	# grid = [
	#   " /",
	#   "/ "
	# ] 
	# print(regionsBySlashes(grid))
#	grid = [
#	  " /",
#	  "  "
#	]
#
#	print(regionsBySlashes(grid))
#
#	grid = [
#	  "/\\",
#	  "\\/"
#	]
#	print(regionsBySlashes(grid))

	grid = [
	  "//",
	  "/ "
	]

	print(regionsBySlashes(grid))
	print("END OF TESTING...")



main() 




