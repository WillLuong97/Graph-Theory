#Leetcode 785. Is Graph Bipartite?

#Problem statement: 
'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to divide the set of nodes into two independent subsets.
Constraints:

1 <= graph.length <= 100
0 <= graphp[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected. 
'''
import collections
#function to find if a graph is biparte or not? 
def isBipartite(graph):
    #base case: no graph, not biparte
    if not graph: 
        return False
    
    #visited array to store the node that has been processed
    colored = [0] * len(graph)
    #run BFS through the graph array to process each node
    for node in range(len(graph)):
        #check if particular node has been visited or not
        if colored[node] == 0:
            queue = collections.deque([node])
            colored[node] = 'RED'
        #Pop the node out of the queue and check its neighbor
        while queue:
            popped_node = queue.popleft()
            #store the color of the current node so that we can color the opposite of the popped_node
            curr_color = 'BLUE' if colored[popped_node] == 'RED' else 'RED'
            #loop through the list of neighbor and process each node
            for neighbor in graph[popped_node]:
                #check if the neighbor has been vistied or not
                if colored[neighbor] == 0:
                    queue.append(neighbor)
                    #colored the neighbor with the opposite color of the parent node
                    colored[neighbor] = curr_color
                #base case: return false if the neighbor cannot be colored, this could be because that the graph is not biparte.
                elif colored[neighbor] != curr_color:
                    return False


    return True

#Time complexity: O(V+E) as this is the typical time complexity for a BFS.
                    
#main function: 
def main():
    print("TESTING IS GRAPH BIPARTE...")
    test_graph_01 = [[1,3],[0,2],[1,3],[0,2]]
    test_graph_02 = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(isBipartite(test_graph_01))
    print(isBipartite(test_graph_02))
    print("END OF TESTING...")

main()