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



[ "0 1 "
  "0 1 "
]

observation: if the same slashes are diagonal to each other then it can be combined together and divide a bigger region, matrix[i-1][j-1] == matrix[i][j]

Otherwise, 

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

We will apply dfs to solve this problem by converting each slashes into a 1, regardless of its being backwards or forwards. 
Example: 
"/"
0 0 1
0 1 0
1 0 0 
To do this, we will create a new matrix with the same dimension as the array of string but add in extra borders, which are all 0's

with 1 being the slashes or line and 0's being the open space, we will apply dfs to count the connected components of 0s and retunr the final number

'''
#helper method to perform dfs on the updated grid to find connected 0s parts: 
def dfs(matrix, i, j):
	#check to see if the node is valid or not
	#1st - not a border but still within the boundary 
	if i >= 0 and i < len(matrix) and  j >= 0 and j < len(matrix) and matrix[i][j] == 0:
		#another way of keeping track of the visited element, by making it equal to 1, we will ignore in the algorithm, when we backtrack 
		matrix[i][j] = 1
		#branch out to the neighboring node recursively
		dfs(matrix, i+1,j)
		dfs(matrix, i, j+1)
		dfs(matrix, i, j-1)
		dfs(matrix, i-1, j)
		#finding the connected component, the connected component are 0s that are sitting right next to each other
		if i%2 != j%2:
			dfs(matrix, i+1, j+1)
		if i%2 == j%2:
			dfs(matrix, i+1, j-1)
		if i%2 != j%2:
			dfs(matrix, i-1, j-1)
		if i%2 == j%2:
			dfs(matrix, i-1, j+1)
		
def regionsBySlashes(grid):
	#bsae case: 
	if not grid or not len(grid):
		return 0 
	
	count = 0
	#getting the row and column of the matrix
	m = len(grid)
	n = len(grid[0])
	#create a new grid to store 0 and 1 representation of the slashes
	#the matrix has twice the length because of the extra border built in
	zero_one_grid = [[0 for j in range(2*m)] for i in range(2*m)]
	#adding 1 to the grid 
	for i in range(m):
		for j in range(m):
			#converting the slashes into a one
			if grid[i][j] == "/":
				zero_one_grid[2*i][2*j+1] = 1
				zero_one_grid[2*i+1][2*j] = 1
			if grid[i][j] == "\\":
				zero_one_grid[2*i][2*j] = 1
				zero_one_grid[2*i+1][2*j+1] = 1
	for i in range(len(zero_one_grid)):
		for j in range(len(zero_one_grid)):
			if zero_one_grid[i][j] == 0:
				count += 1
				dfs(zero_one_grid, i, j)
	return count
				
	
#Main function to run the test cases: 
def main():
	print("TESTING REGIONS CUT BY SLASHES...")
	grid = [
	  " /",
	  "/ "
	] 
	print(regionsBySlashes(grid))
	grid = [
	  " /",
	  "  "
	]

	print(regionsBySlashes(grid))

	grid = [
	  "/\\",
	  "\\/"
	]
	print(regionsBySlashes(grid))

	grid = [
	  "//",
	  "/ "
	]

	print(regionsBySlashes(grid))
	print("END OF TESTING...")

main() 

