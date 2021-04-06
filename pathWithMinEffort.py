#Problem 1631. Path With Minimum Effort
'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

Appraoch: 
Create a dictionary to store each cell with the effort to get from the starting point to that cell. The idea is that after the algorithm is finsished, 
we should have an dictionary that have all calculated maximum efforts from the starting point to the current cell. 

'''
from collections import deque
def minimumEffortPath(heights):
	#base case:
	if not len(heights):
		return None	
	m = len(heights)
	n = len(heights[0])
	#dictioanry to store the coordiate of a cell and the effort value to get there from the starting cell
	cell_efforts = {(0,0): 0}
	queue = deque([(0,0)])
	while queue:
		#pop element out from the queue to process
		x, y = queue.popleft()
		
		#branching out to the neighboring node with the right path
		for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
			new_x = x + dx
			new_y = y + dy
			
			#check to make sure that the path are within the boundary
			if not(0 <= new_x and new_x < m and 0 <= new_y and new_y < n):
				continue
			#calculate the effort to get to the current cell
			effort = max(cell_efforts.get((x,y)), abs(heights[new_x][new_y] - heights[x][y]))
			
			#if the cell already exist and its effort is lesser than the calcualted effort, then skip it, 
			#because we only care about the path with the least maximum effort
			if(new_x, new_y) in cell_efforts and cell_efforts[(new_x, new_y)] <= effort:
				continue 

			cell_efforts[(new_x, new_y)] = effort
			queue.append((new_x,new_y))

	if (m-1, n-1) not in cell_efforts:
		return -1
	return cell_efforts[(m-1, n-1)]

#Main function to run the test cases:
def main():
	print("TESTING Minimum Effort Path...")
	heights = [[1,2,2],[3,8,2],[5,3,5]]
	print(minimumEffortPath(heights))
	heights = [[1,2,3],[3,8,4],[5,3,5]]
	print(minimumEffortPath(heights))
	heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
	print(minimumEffortPath(heights))

	print("END OF TESTING...")

main()
