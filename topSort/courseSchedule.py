#207. Course Schedule
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''
from collections import defaultdict
from collections import deque
#Perform topological sort on the prerequsitse array, with the the prereq comes before the required class. If the final order array has the same length as the the numCourses, then return True. Otherwise, if there
# is cycle in the prereq class, meaning the class is repeated, then also return false. 
def canFinish(numCourses, prerequisites):
	if not numCourses:
		return False
	#a dictionary to store the adjacency list of the graph prereq
	graph = defaultdict(list)
	for required, prereq in prerequisites:
		graph[required].append(prereq)
	#array to store all the value that has been visited
	visited = set()
	#the final stack to return after dfs has been recursively traverse through all the node
	stack = deque()
	#the current stack to store each node as the dfs is still checking its neighbor
	stack_contains = set()
	#helper method to perform dfs on the graph
	#this function return True if there is a cycle, otherwise create a stack to store the topological order of the graph. 
	def dfs(node):
		#once we are looking at each node, pass them onto the stack
		visited.add(node)
		stack_contains.add(node)
		#check for its neighbor, if there is a cycle, return True
		for neighbor in graph.get(node, []):
			#check to see if there is a cycle or not
			if neighbor in visited and neighbor in stack_contains:
				return True
			if neighbor not in visited and dfs(neighbor):
				return True
		stack.append(node)
		stack_contains.discard(node)
		return False

	#loop through the graph, and pass in any unvisited node
	for i in range(numCourses):
		if i not in visited:
			result = dfs(i)
			#if there is a cycle
			if result: return False

	return True
#Main function to run the test cases: 
def main():
	print("TESTING COURSE SCHEDULE...")
	#test cases: 
	numCourses_1 = 2
	prereq_1 = [[1,0]]
		
	numCourses_2 = 2
	prereq_2 = [[1,0], [0,1]]
	print(canFinish(numCourses_1, prereq_1))
	print(canFinish(numCourses_2, prereq_2))

	print("END OF TESTING...")

main()
