#Python3 implementation of graph data structure using an adjacenct list of of the graph 

#Graph node structure
class Vertex: 
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None    #neighbor of the current node


#A class to represent a graph
class Graph:
    #the graph will recieve a number of vertices and then intialize an empty graph from the number of nodes
    def __init__(self,numOfVertices):
        self.V = numOfVertices
        self.graph = [None] * self.V

    #Function to add an edge into an undirected graph
    def addEdge(self, src, dest):
        #adding the node into the source node
        destVertex = Vertex(dest)
        #since there is an edge between the two vertices, set the neighbor of destination vertext to the source vertex
        destVertex.next = self.graph[src]
        self.graph[src] = destVertex

        #since this graph is unweighted, the source vertext would also receive a neighbor relationship from the destination vertex
        srcVertex = Vertex(src)
        srcVertex.next = self.graph[dest]
        self.graph[dest] = srcVertex

    #Function to print out the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertices {}\n".format(i), end="")
            temp = self.graph[i]
            while temp: 
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


#main function to display the graph
def main():
    numOfVertices = 5

    graph = Graph(numOfVertices)
    graph.addEdge(0, 1) 
    graph.addEdge(0, 4) 
    graph.addEdge(1, 2) 
    graph.addEdge(1, 3) 
    graph.addEdge(1, 4) 
    graph.addEdge(2, 3) 
    graph.addEdge(3, 4) 
    print("GRAPH CREATED: ")
    graph.print_graph()    
    print("END OF PROGRAM...")

main()
        

        
        
        