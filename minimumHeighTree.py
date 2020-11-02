#Leetcode 310: Minimum height spanning trees 

#Problem statement: 

'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
'''

'''
Time Complexity: 
Let |V|∣V∣ be the number of nodes in the graph, then the number of edges would be |V| - 1∣V∣−1 as specified in the problem.

Time Complexity: \mathcal{O}(|V|)O(∣V∣)

First, it takes |V|-1∣V∣−1 iterations for us to construct a graph, given the edges.

With the constructed graph, we retrieve the initial leaves nodes, which takes |V|∣V∣ steps.

During the BFS trimming process, we will trim out almost all the nodes (|V|∣V∣) and edges (|V|-1∣V∣−1) from the edges. Therefore, it would take us around |V| + |V| - 1∣V∣+∣V∣−1 operations to reach the centroids.

To sum up, the overall time complexity of the algorithm is \mathcal{O}(|V|)O(∣V∣).

Space Complexity: \mathcal{O}(|V|)O(∣V∣)

We construct the graph with adjacency list, which has |V|∣V∣ nodes and |V|-1∣V∣−1 edges. Therefore, we would need |V| + |V|-1∣V∣+∣V∣−1 space for the representation of the graph.

In addition, we use a queue to keep track of the leaves nodes. In the worst case, the nodes form a star shape, with one centroid and the rest of the nodes as leaves nodes. In this case, we would need |V|-1∣V∣−1 space for the queue.

To sum up, the overall space complexity of the algorithm is also \mathcal{O}(|V|)O(∣V∣).


'''

#Function to create the solution:
#BFS + Centroid approach: trim all the leaf nodes until we find the centroid, which is the node with the smallest connection
def findMinHeightTrees(n, edges):
    #base case: there is no more than 2 centroid in any graph
    if n <= 2:
        return [i for i in range(n)]

    #build the graph from the edge list: 
    neighbors = [set() for i in range(n)]
    for startNode, endNode in edges:
        #create a connection between between the node, since the graph are undirected, startNode and endNode are both neighbors
        neighbors[startNode].add(endNode)
        neighbors[endNode].add(startNode)
    #appending the leaves node into the list
    leaves = []
    for i in range(n):
        #the condition of a leaves node only has 1  neighbors
        if len(neighbors[i]) == 1:
            leaves.append(i)

    #keep track of the remaining nodes after each trim
    remainingNode = n
    while remainingNode > 2: 
        #trimming the leaves nodes
        remainingNode -= len(leaves)
        new_leaves = []
        #after trimming the leave node, we must also trim the edge that connect to those leave node as well 
        while leaves:
            leaf = leaves.pop()
            #destroy the edge connection by removing the edge(neighbor relationship) from the leaf node with its neighbors
            for neighbor in neighbors[leaf]:
                neighbors[neighbor].remove(leaf)
                #repeat this steps until all outer layer of leaf node has been cut and move onto the next set of leaf node
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves




#Main function to execute the program 
def main():
    print("TESTING MINIMUM HEIGHT SPANNING TREE...")
    test_n = 6
    test_edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    test_n01 = 1
    test_edges01 = []

    test_n02 = 2
    test_edges02 = [[0,1]]

    print(findMinHeightTrees(test_n, test_edges))
    print(findMinHeightTrees(test_n01, test_edges01))
    print(findMinHeightTrees(test_n02, test_edges02))
    print("END OF TESTING...")
main()