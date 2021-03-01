#Problem 1765. Map of Highest Peak
'''
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
Example 1:
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:
Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.


Using BFS, we will look at each cell and then its neighbor to determin how much heights can it be assigned to while maintaining the 3 conditions
We also give preference to the water cell first since its value is always 0 we can use it to determine the other cells better.
'''
def highestPeak(isWater):
	row = len(isWater)
	col = len(isWater[0])
	result = [[-1 for i in range(col)] for j in range(row)]
	visited = [[False for i in range(col)] for j in range(row)]
	#a queue to keep track of each cell being processsed
	queue = []
	#Helper method to run bfs through the matrix and determine the heights
	def bfs(visited, result, queue):
		while len(queue) > 0:
			#get the latest cell being processed
			current_cell = queue.pop(0)
			row = current_cell[0]
			col = current_cell[1]
			#vaiid locations: 
			dx = [0,0,1,-1]
			dy = [1,-1,0,0]
			for i in range(len(dx)):
				#getting the coordinate of the current cell neighbors
				new_row = row + dx[i]
				new_col =  col + dy[i]
				#assigning the heights to the current cell based on its neighbor
				if new_row >= 0 and new_row < len(visited) and new_col >= 0 and new_col < len(visited[0]) and not visited[new_row][new_col]:
					visited[new_row][new_col] = True
					#assign the height: 
					result[new_row][new_col] = result[row][col] + 1
					queue.append((new_row, new_col))

	#loop through the matrix to check for each cells but we want to begin each check with a water cell
	for i in range(row):
		for j in range(col): 
			#found a water mass:
			if isWater[i][j] == 1:		
				result[i][j] = 0
				visited[i][j] = True
				queue.append((i,j)) 

	bfs(visited, result, queue)
	return result
#Main function to run the test cases:
def main():
	print("TESTING MAP OF HIGHEST PEAK...")
	#test cases: 
	isWater = [[0,1],[0,0]]
	print(highestPeak(isWater))
	isWater = [[0,0,1],[1,0,0],[0,0,0]]
	print(highestPeak(isWater))

	isWater = [[0,0],[1,1],[1,0]]
	print(highestPeak(isWater))


	print("END OF TESTING....")


main()
