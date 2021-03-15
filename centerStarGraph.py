#Problem 1791. Find Center of Star Graph
'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
Constraints:
3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
'''
def findCenter(edges):
	#base case:
	if not len(edges):
		return None
	#extracting the first set of nodes from the first edge
	u = edges[0][0]
	v = edges[0][1]
	#loop through the rest of the edges to find the center node
	for edge in edges:
		if u not in edge:
			u = 0 
		if v not in edge:
			v = 0
	if u != 0:
		return u
	if v != 0:
		return v



#Main function to run the test case: 
def main():
	print("TESTING FIND CENTER OF A STAR GRAPH...")
	#Test case: 
	edges =[[1,2],[2,3],[4,2]]
	print(findCenter(edges))
	edges = [[1,2],[5,1],[1,3],[1,4]]
	print(findCenter(edges))
	print("END OF TESTING...")

main()
