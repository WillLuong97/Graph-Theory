# Topological Sort

## Definition: 
- The topological sort is an algorithm that can find a topological ordering in O(v+e) time!
- A topological ordering is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A appears before node B in the ordering 
- Note: Topological ordering are not unque, there are multiple ways that an ordering can be made. 
- The graph must always be a directed acylic graph. Every node is depended on each other, if if there is a cycle, the some node would always stuck in a loop. 

### How do I that my graph does not contain a directed cycle? 

- One method is to use Tarjan's strongly connected components algorithm, which can be used to find these cycles

### Special Case: 

- A tree is also considered to be a DAG, because it has no cycles, and TopSort can be applied on it 
- To apply TopSort, start by picking the leaf nodes and work your way to the root. 



## Topological Sort Algorithm: 

- Pick an unvisited node

- Beginning with the selected nodes, do a Depth First Search (DFS), exploring only unvisited nodes. 

- On the recursive callback of DFS, add the current node to the toplogical sort odering in reverse order. 

## Pseudocode: 

```
#assumption: graph is stored as an adjacency list
function topsort(graph):
	N = graph.numberOfNodes()
	V = [false,...,false] #lenght of N
	ordering = [0,...,0] #lenght of N
	i = N - 1 #Index of ordering array

	for(at = 0; at < N; att++): 
		if V[at] == false: 
			#array to store all the nodes created from the dfs
			visitedNode = []
			dfs(at, V, visitedNodes, graph)
			for nodeID in visitedNodes: 
				ordering[i] = nodeID
				i = i - 1
	return ordering

#helper method to run dfs through the graph
function dfs(at, V, visitedNodes, graph):
	#marking the value we are running is true
	V[at] = true	
	edges = graph.getEdgesOutFromNodes(at)
	for edge in edges: 
		if V[edge.to] == false:
			dfs(edge.to, V, visitedNodes, graph)
	visitedNode.add(at)
```
## Application: 
- Many real world application such as: 
	+ School class prerequisites
	+ Program dependecies
	+ Event Scheduling
	+ Assembly instructions
	+ etc...
