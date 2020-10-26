#1042. Flower Planting With No Adjacent


#Problem statement: 
'''
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes the existence of a bidirectional path from garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

There is no garden that has more than three paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Constraints:

1 <= n <= 104
0 <= paths.length <= 2 * 104
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
No garden has four or more paths coming into or leaving it.

'''
from collections import defaultdict
#Function to solve the problem: 
def gardenNoAdj(N, paths):
    #base case: 
    if not N: 
        return None

    if N == 1:
        return [1]
    #visited array to store the any processed garden
    planted = [0] * (N+1)
    setOfFlowers = [1,2,3,4]

    pathDict = defaultdict(list)
    #create a dictionary to store the garden and its neighboring gardens
    for garden, neighbor in paths:
        pathDict[garden].append(neighbor)
        pathDict[neighbor].append(garden) 

    #helper method to perform dfs algorithm on the give garden
    def dfs(garden, pathDict, planted):
        #check to see if the garden has already planted a flower or not
        if planted[garden] > 0:
            return

        #check for any flower that cannot be planted by going through the list of its neighboring garden and check to see what flower is already planted there
        offLimitFlower = set([planted[flower] for flower in pathDict[garden] if planted[flower] >0])

        #if all the off limit flower exceed the total number of flower variety, then we cannot plant a flower here
        if len(offLimitFlower) == len(setOfFlowers):
            return False

        #loop through the list of flowers set and assign a flower to the current garden
        for flower in setOfFlowers:
            #if the flower has been planted by its neighbor already, then backout
            if flower in offLimitFlower: 
                continue

            #otherwise, assign the flower to the current garden
            planted[garden] = flower
            #Boolean to check if the current flower can be used to plant in this current garden
            canPlant = True
            for neighbor in pathDict[garden]:
                if not dfs(garden, pathDict, planted):
                    canPlant = False
                    break
            if canPlant:
                return True 
        return False
    #Loop through the path array and processed each garden
    for garden in range(1, N+1):
        dfs(garden, pathDict, planted)

    return planted[1:]



#main fucnction to run the program 
def main():
    print("TESTING PLANT FLOWER WITH NO ADJACENT")
    n_1 = 3
    path_1 =[[1,2],[2,3],[3,1]]

    n_2 = 4
    path_2 = [[1,2],[3,4]]

    n_3 = 4
    path_3 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    print(gardenNoAdj(n_1, path_1))
    print(gardenNoAdj(n_2, path_2))
    print(gardenNoAdj(n_3, path_3))


    print("END OF TESTING...")
main()