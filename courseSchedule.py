#207. Course Schedule

#Problem statement: 

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

'''
#time complexity: O(N) the dfs is done to check on all node in the graph, n is the number of courses
#space complexity: O(N) the recursion stack will run until in the graph has been checked.
from collections import defaultdict
#we will solve this program using DFS graph traversal:
def canFinish(numCourses, prerequisites):
    #base case: 
    if not numCourses:
        return False

    #A dictionary to store the graph nodes and its neighbors in the adjaecny list format
    #{1: [2,3,4]}
    graphNodeDict = defaultdict(list)
    for node, neighbor in prerequisites:
        graphNodeDict[node].append(neighbor)
    
    #an array to store the state of each node: 
    #nodeState[node] == -1: In the process of looking at a particular graph node
    #nodeState[node] == 1: The node has been done processing and there is nothing else to look for 
    #nodeState[node] == 0: The graph node has not yet been processed. 
    nodeState = [0] * numCourses

    #helper method to run dfs throuhg the graph to see if there is a 
    #cycle between each node or not, if there is, return a false, as there is no way to finish the courses
    def dfs(node):
        #if the current node returns a 1, meaning, there is no cycle
        if nodeState[node] == 1:
            return False

        #if the current node equals to a -1, there is a cycle
        if nodeState[node] == -1:
            return True 

        #if not, set the current node -1 as we are looking at it 
        nodeState[node] = -1
        #loop through the neighbor list of the current node and apply dfs recursively through them
        #to check if there is any cycle back to the current node
        for i in graphNodeDict[node]:
            if dfs(i):
                return True

        nodeState[node] = 1
        return False

    for i in range(numCourses):
        #loop through the element in prereq list and as long as there is a cycle, return false
        if dfs(i):
            return False

    return True 



'''
Leetcode: 210 Course Schedule II

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

'''
def findOrder(numCourses , prerequisites):
    #base case: 
    if not numCourses: 
        return []

    if not prerequisites:
        return [0]

    #result array that would store the path: 
    path = []
    

            
#main function to run the program
def main():
    print("TESTING COURSE SCHEDULE...")
    test_num_courses_0 = 2
    test_prereq_0 = [[1,0]]
    test_num_courses_1 = 2
    test_prereq_1 = [[1,0],[0,1]]
    print(canFinish(test_num_courses_0, test_prereq_0))
    print(canFinish(test_num_courses_1, test_prereq_1))

    print("")
    print("TESTING COURSE SCHEDULE II...")
    
    print("END OF TESTING...")

main()