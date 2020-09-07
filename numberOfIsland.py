#Python program to solve Leetcode 202. Number of Island using Depth First Search 

'''
Problem statements: 
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''

'''
Algorithm: We will solve this problem using the deapth first search method, to do so, we will loop through the
grid map once and each time we loop through, we will check to whehter the current element is 1 or 0, if 1 we will 
record it but 0 we will ignore it. In adidtion, we also keep track of each visited element so that we do not have to check the same element twice as we go through the array.

At the end, if the element is already visited, or if it is a 0 or if it does not have any neighbors that are 1, then we will exit out of the algorithm and count the number of island by 1

1. Create a visited array and initialized it to False, so each time we visit a node, we will note it in the vistited array as True, which mean we have seen it before
2. 
3. 
4. 

'''

def numIsland(grid):
    #Base case: the grid is empty, so we return 0
    if not grid: 
        return 0
    visited = [[False for i in range(0, len(grid))] for j in range(0, len(grid[0]))]
    numOfIsland = 0

    #loop through the grid map to look at each element and check whether it is 1 or 0: 
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if(not visited[i][j] and grid[i][j] == "1"):
                #run dfs on the element
                dfs(i, j, visited, grid)
                numOfIsland += 1

    return numOfIsland

#Helper method to check for the neighbor of the current element to see if it is a 1 or 0
#the function will collect all possible 1 that are grouped together
def dfs(row, column, visited, grid):
    #the element is checked
    visited[row][column] == True

    #List of possble that we can use to traverse the grid map
    #up, down, left , right
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    for move in moves: 
        newRow = row + move[0]
        newCol = column + move[1]

        if(isValidMove(newRow, newCol, grid) and not visited[newRow][newCol] and grid[newRow][newCol] == '1'):
            dfs(newRow, newCol, visited, grid)

#Helper method to check if the row and column moves the right way
def isValidMove(row, column, grid): 
    return (row >= 0 and column >= 0 and row < len(grid) and column < len(grid[0]))



#driver code to run the function
def main():
    print("TESTING NUMBER OF ISLAND...")
    test_grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    print(numIsland(test_grid))

    print("END OFT TESTING...")
main()