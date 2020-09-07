# Graph-Theory

## Introduction: 

 - Graph theory is the mathematcial theory of the properties and applications of graphs (networks)
 
 - Graph can be used to represent any kind of problems. For example, social networks of friends or combination of different items. 
 
 ## Types of Graphs: 
 
 1. Undirected Graph: is graph in which edges have no orientation/directions and can drawn either ways. the edge (u,v) is identical to the edge  (v,u)  
 2. Directed Graph: is a graph in which edges jave ORIENTATION/DIRECTION. For example, the edge (u,v) is the edge from node u to node v.   
 3. Weighted graphs: many graphs can contain certain weight to represent arbitrary value such as cost, distance, quantity, etc. 
 
 ### Special graphs: 

+ Tree: is an undirected graph with no cycles. Equivalently, it is a connected graph with N nodes and N-1 edges. 

+ Rooted Tree: is a tree with a designated root node where every edge either points away from or towards the root node. 

    + Arborescene (out-tree) is when edges point away from the root of the graph
    + Anti-arborescene (in-tree) is when edges point toware the root of the graph 
    
    + Directed Acyclic Graphs (DAGs): are directed graphs with no cycles. These graphs play a vital role in representing structures with dependencies . All out-trees are DAGs but not all DAGs are out-trees

+ Bipartite Graph: is one whose vertices can be split into two independent groups U, V such that every edge connects U and V

+ Complete Graphs: is one where there is a unique edge between every pair of nodes. A complete graph with n vertices is denoted as the graph Kn. 

## Representing Graphs: 

Adjacency matrix: is a very simple way to represent a graph. The idea is that the cell m[i][j] represents the edge weight of going from node i to node j. 

Pros: 
+ Space efficient for representing dense graphs 
+ Edge weight lookup is O(1)
+ Simplest graph representation
    
Cons: 
+ Requires 0(V^2) space
+ Iterating over all edges takes O(V^2) time
 
 
 Adjacency list: is a way to represent a graph as a map from nodes to list of edges. 
```
Example: A -> [(B,4), (C, 1)]
               B ->  [(C, 6)]
               C -> [(A, 4), (B, 1), (D, 2)]
               D -> []
```
Pros: 
+ Space efficient for representing sparse graphs 
+ Iterating over all edges is efficient

Cons:
+ Less space efficient for denser graph. 
+ Edge weight lookup is O(E)
+ Slightly more complex graph representation


- Edge list: a way to represent a graph simply as an unordered list of edges. Assume the notation for any triplet (u,v,w) means: "the cost from node u to node v is w". However, this representation is seldomly used
because it is not structured 

Pros: 
+ Space efficient for representing sparse graphs
+ Iterating over all edges is effcient 
+ Very simple structure 

Cons: 
+ Less space efficient for denser graph 
+ Edge weight lookup is O(E)

## Common Graph Theory Problems

Before solving the problems, ask yourself these question: 

1. Is the graph directed or undirected? 
2. Are the edges of the graph weighted? 
3. Is the graph I will encounter likely to be sparse or dense with edges? 
4. Should I use an adjacency matrix, adjacency list, an edge list or other structure to represent the graph efficiently? 


### Shortest path problem: 

Given a weighted graph, find the shortest path of edges from node A to node B

Algorithms: BFS (unweighted graph), A*, Dijkstras, Bellman-ford, etc. 

### Connectivity: 

Does there exist a path between node A and node B? 

Typical solution: Use union find data structure or any search algorithm (DFS)

### Negative cycles: 

Does my weighted digraph have any negative cycles? If so, where?   

Algorithms: Bellman-Ford and Floyd-Warshall 


### Strongly Connected Components

Strongly Connected Components (SCCs) can be thought of as self-contained cycles within a directed graph where every vertex in a given cycle can reach every other vertex in the same cycle 

Algorithm: Tarijan's and Kosaraju's algorithm

### Travelling Salesman Problem:

Given a list of cities and the distance between each pair of cities, what is the shortest possible route that visit each city exactly once and returns to the origin city? 

Algorithm: Held-Karp, branch and bound and many approximation algorithms

The TSP problem is NP-Hard meaning it s very computationally challenging problem. 

### Bridges: 

A bridge/ cut edge is any edge in a graph whose removal increases the number of connected components. 

Bridges are important in graph theory because they often hint at weak points, bottleneck or vulnerabilities in a graph 

### Articulation points: 

An articulation points / cut vertex is any node in a graph whose removal increases the number of connected components.

Articulation points are important in graph theory because they often hint at weak points, bottlenecks or vulnerabilities in a graph.


### Minimum Spanning Tree (MST)

A minimum Spanning Tree is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. 

Algorithms: Kruskal, Prim's Boruvka's Algorithm 

MST are seen in many applications including: Designing a least cost network, circuit design, transporation networks, and etc. 


### Network Flow:  Max Flow

With an infinite source how much "flow" can we push through the network? 

Suppose the edges are roads with cars, pipes with water or hallways with packed with people. Flow represents the volume of water allowed to flow through 
the pipes, the number of cars the roads can sustain in traffic and the maximum amount of people that can navigate through the hallways 

Algorithms: Ford-fulkerson, Edmonds-Karp and Dinic 's algorithm 

