#Problem 743: Network Delay Time

'''
Problem statement: 
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

'''
from collections import defaultdict
#Depth first search approach: 
def networkDelayTime_DFS(times, N, K):
    #base case: no times, no N and K, nothing to return
    if not times or not N or not K: 
        return -1
    graph = defaultdict(list)
    timeDict = {}
    # timeDict = {node: float('inf') for node in range(1, N+1)}

    #create a dictionary to store the node/neighbor relationship of the times list
    for u,v,w in times:
        graph[u].append((w,v))

    # #Create a dictionary to store the time for the network to reach each node
    for i in range(1, N+1):
        timeDict[i] = float('inf')

    #create a helper method to run the dfs algorithm through the network layer
    def dfs(node, cost):
        #if the cost we are checking is greater than the cost currently in the time 
        #cost dictionary, the break this 
        if cost >= timeDict[node]: return 

        #update the node with its cost in the array
        timeDict[node] = cost
        #loop through the neighbor of the current node to check on the rest on the next network node 
        for nodeTime, node in sorted(graph[node]):
            dfs(node, cost + nodeTime)
    dfs(K, 0)
    answer = max(timeDict.values())
    return answer if answer < float('inf') else -1

        
#Time complexity: 
#Space complexity: O(N+E), the size of the graph O(E) with the size of the recursion call stack to our DFS O(N)
    



#main function to test out the program
def main():
    print("TESTING NETWORK DELAY TIME...")
    #TEST VALUE: 
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    print(networkDelayTime_DFS(times, N, K))
    print("END OF TESTING...")
main()