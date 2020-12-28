#Leetcode 1162. As Far from Land as Possible

'''
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

'''
def maxDistance(grid):
    #base case: 
    if not len(grid):
        return None
    m = len(grid)
    n = len(grid[0])
    visited = [[False for i in range(m)] for j in range(n)]
    queue = []
    localDistance = [[0 for i in range(m)] for j in range(n)]
    #valid position: 
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    #loop through the grid to find the node 1 and run the dfs on all the water node 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                visited[i][j] = True
                queue.append((i,j,0))
    if len(queue) == 0 or len(queue) == len(grid) * len(grid[0]):
        return -1
    max_distance = 0
    while queue:
        #loop through the level of the queue
        starting_point = queue.pop(0)
        for index in range(len(dx)):
            new_x = starting_point[0] + dx[index]
            new_y = starting_point[1] + dy[index]
            current_distance = starting_point[2]
            #make sure that the new moves are within in the grid. 
            if 0 <= new_x < m and 0<= new_y < n and grid[new_x][new_y] == 0:
                next_level = current_distance + 1
                grid[new_x][new_y] = next_level
                queue.append((new_x, new_y, next_level))
                max_distance = max(max_distance, next_level)
    return max_distance

def main():
    print("TESTING AS FAR FROM LAND AS POSSIBLE...")
    grid_01 = [[1,0,1],[0,0,0],[1,0,1]]
    grid_02 = [[1,0,0],[0,0,0],[0,0,0]]
    print(maxDistance(grid_01))
    print(maxDistance(grid_02))
    print("END OF TESTING...")
main()