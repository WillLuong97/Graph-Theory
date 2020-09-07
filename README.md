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

- Adjacency matrix: is a very simple way to represent a graph. The idea is that the cell m[i][j] represents the edge weight of going from node i to node j. 

Pros: 
+ Space efficient for representing dense graphs 
+ Edge weight lookup is O(1)
+ Simplest graph representation
    
Cons: 
+ Requires 0(V^2) space
+ Iterating over all edges takes O(V^2) time
 
 
 - Adjacenct list: is a way to represent a graph as a map from nodes to list of edges. 
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


