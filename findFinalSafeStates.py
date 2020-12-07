#Leetcode 802. Find Eventual Safe States
'''
Problem statement:
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
'''
# function to solve the solution: 
# Coloring approach: the idea is to dfs until a cycle is found, then break and check the next node, if the cycle is not found and we color the rest of the node with the same color
# Gray: the first color
# Black: the exit color
# White: has not been colored
from collections import defaultdict
def eventualSafeNodes(graph):
    #base case: 
    if not graph:
        return None
    #coloring options:
    WHITE, GRAY, BLACK = 0,1,2
    #dictionary of colored node
    color = defaultdict(int)
    #helper method to run the dfs algorithm:
    #return true to make sure 
    def dfs(node):
        #if we encounter a cycle, then the current node is not white, meaning it has been colored
        #we black it out and return it 
        if color[node] != WHITE:
            return color[node] == BLACK 
        
        color[node] = GRAY
        #loop through the neighbor of the current node and repeat the coloring process
        for neighbor in graph[node]:
            if color[neighbor] == BLACK:
                continue 
            if color[neighbor] == GRAY or not dfs(neighbor):
                return False
        color[node] = BLACK
        return True

    return filter(dfs, range(len(graph)))
#Main function to run the program: 
def main():
    print("TESTING FIND FINAL SAFE STATES....")
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(eventualSafeNodes(graph))
    print("END OF TESTING...")
main()