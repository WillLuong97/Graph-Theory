#Python3 Implementation of Breadth First Search algorithm in Graphs
'''
Breath-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. BFS can be easily implemented using recursion and data structures like dictionaries and lists.

The Algorithm
Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
If there are no remaining adjacent vertices left, remove the first vertex from the queue.
Repeat step 1 and step 2 until the queue is empty or the desired node is found.

'''
def bfs(graph):
    #base case: 
    if not graph:
        return None
    
    visited = []
    queue = []
    #helper method to traverse the graph using the bfs
    def helper(visited, node, graph):
        if node in visited: 
            return
        visited.append(node)
        queue.append(node)
        #the queue is used to process each node                
        while queue:
            current = queue.pop(0)
            print(current)
            for neighbors in graph[current]:
                if neighbors not in visited:
                    visited.append(neighbors)
                    queue.append(neighbors)

    
    helper(visited, 'A', graph)


#main function to run the test cases: 
def main():
    print("TESTING BREADTH FIRST SEARCH ALOGRITHM...")
    graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
    bfs(graph)
    print("END OF TESTING...")
main()