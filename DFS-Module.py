#Module to perform how to traverse a graph using DFS

'''
Depth First Seach: 
Time complexity: O(V+E), V is the number of vertices, and E is the number of edges.  
Space complexity: O(m), m is the length of the longest path For each node, you have to store its siblings so that when you have visited all the children, and you come back to a parent node, you can know which sibling to explore next.

'''
#Function to traverse the graph using dfs
def dfs(matrix, visited, node):
	#check if the node has been visited or not
	if node not in visited: 
		print(node)
		visited.add(node)
	#branch out to its neighbor and go through the process recursively
	for neighbor in matrix[node]:
		dfs(matrix, visited, neighbor)	

#Main function to run test dfs:
def main():
	print("PRINTING OUT ALL GRAPH NODE USING DFS...")

	graph = {
	    'A' : ['B','C'],
	    'B' : ['D', 'E'],
	    'C' : ['F'],
	    'D' : [],
	    'E' : ['F'],
	    'F' : []
	}
	#set to keep track of visited node
	visited = set()
	print("Node returns: ")
	print(dfs(graph, visited, 'A'))

	print("END OF TESTING...")


main()
