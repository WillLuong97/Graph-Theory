#Problem 1267. Count Servers that Communicate
'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''
def countServers(grid):
	#setting up row and column
	m = len(grid)
	n = len(grid[0])
	visited = set()
	#Function to get the neighboring server. 
	def getNeighbors(row, col, grid):
		#this set will contain all server, 1 and 0 from the grid into a set for easier checking in dfs
		nodes = set()
		#getting all server in the same row
		for i in range(n):
			nodes.add((row, i))
		for j in range(m):
			nodes.add((j, col))
		nodes.discard((row, col)) 
		return nodes
		
	#dfs to look through each nodes in the array and check for its visited
	def dfs(i, j, grid, visited):
		#looking at the neighbor of the current node
		for neigh in getNeighbors(i, j, grid):
			x, y = neigh
			if neigh not in visited and grid[x][y] == 1:
				visited.add(neigh)

	#loop through the grid and run dfs on node that contain an acutal server to see if it can be connected to other server
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				dfs(i,j, grid, visited)
	return len(visited)
#Time complexity: O(mxn), m is the number of node in the row and n is the number of nodes in the col
#Space complexity:  O(n), where n is the length of the visited array
	
			
#Main function to run the test cases:
def main():
	print("TESTING COUNT SERVERS THAT COMMUNICATE...")
	#test cases: 
	grid = [[1,0],[0,1]]
	print(countServers(grid))
	grid =[[1,0],[1,1]]
	print(countServers(grid))
	grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
	print(countServers(grid))
	print("END OF TESTING...")
main()
