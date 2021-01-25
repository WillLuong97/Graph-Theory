#Python3 implementation of topological sort, this file will cover basic implemtation of graph and topsort ordering of a particular graph
'''
- The topological sort is an algorithm that can find a topological ordering in O(v+e) time!
- A topological ordering is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A appears before node B in the ordering
- Note: Topological ordering are not unque, there are multiple ways that an ordering can be made.
- The graph must always be a directed acylic graph. Every node is depended on each other, if if there is a cycle, the some node would always stuck in a loop.

'''
from collections import defaultdict
#Implement a graph structure: the graph will be represented using the adjacency list form the dictionary 
class Graph:
	#constructor
	def __init__(self, vertices):
		self.graph_list = defaultdict(list) #the dictionary to store the all the node. 
		self.vertices = vertices #number of vertices in a nodes

	#function to add the edges between two vertices
	def addEdge(self, node, neighbor):
		#add the node and neighbor into the graph together
		#if the current node is not already in the list so we will add it into the list and init its
		#neighbor 
		if node not in self.graph_list:
			self.graph_list[node] = [neighbor]
		#if the current node already exist, then we just need to append to its neighbor list
		else: 
			self.graph_list[node].append(neighbor)
	#function to show the adjencancy list
	def show_edges(self):
		print(self.graph_list)
		for node in self.graph_list:
			for neighbor in self.graph_list[node]:
				print("{ ", node, ": ", neighbor , " }")

	#Function to run topsort on the graph
	#takes in an adjacency list and return an array of top sort ordering
	# {'1': ['2', '3'], '2': ['3', '1'], '3': ['1', '2', '4'], '4': ['3']}
	def topSort(self):
		#base case: 
		if not self.graph_list:
			return []

		visited = [False] * self.vertices
		#a stack to store all current node
		stack = []
		
		#helper method to run the dfs through the graph through recursion
		def dfs(v, visited, stack):
			
			visited[v] = True
			
			for neighbor in self.graph_list[v]:
				if not visited[neighbor]:
					dfs(neighbor, visited, stack)
			stack.insert(0, v)	

		#loop through the adjancey list to process the vertices
		for node_index in range(self.vertices):
			if not visited[node_index]:
				dfs(node_index, visited, stack)
		return stack

 
	
 
#Main function to run the test cases: 
def main():
	print("TESTING TOPOLOGICAL SORT...")
	#implementing the graph
	g = Graph(6)
	g.addEdge(5, 2); 
	g.addEdge(5, 0); 
	g.addEdge(4, 0); 
	g.addEdge(4, 1); 
	g.addEdge(2, 3); 
	g.addEdge(3, 1); 

	g.show_edges()
	print(g.topSort())
	print("END OF TESTING...")
main()

