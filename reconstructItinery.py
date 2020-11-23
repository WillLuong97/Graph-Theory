#Problem 332 - Reconstruct Itinerary
'''
Problem statement: 
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.
'''
#Function to reconstruct the itinery: 
def findItinerary(tickets):
    #base case: 
    if not tickets: 
        return []
    #dictionary to store the node/neighbor relationship between each airport
    flightMap = dict()
    for starting , destination in tickets:
        #if not start positin: 
        if starting not in flightMap: 
            flightMap[starting] = []
        #create a dictionary to store the starting location with its destination  
        flightMap[starting].append(destination)

    #visited dictionary to store which set of flights have been done
    visited = dict()
    result = []
    for starting, destination in flightMap.items():
        #sort the location by lexico order
        flightMap[starting].sort() 
        visited[starting] = [0] * len(flightMap[starting])
    result.append("JFK")
    #call a helper method to perform dfs algorithm to find the flight path from all
    #other airport
    dfs("JFK", visited, flightMap, result, len(tickets))

    return result


#DFS helper method: 
def dfs(starting, visited, flightMap, result, n):
    #base case: 
    if len(result) == n+1:
        return True
    #if the plane starts from a location that is not in our plan, return false
    if starting not in flightMap:
        return False

    #loop through the destination list of the current starting point
    # and then check on its flight path
    for index, end in enumerate(flightMap[starting]):
        #check to see if the current destination has been visited or not: 
        if visited[starting][index] == 0:
            visited[starting][index] = 1
            #if this current destination has not been visited then we will add them to the result list
            result.append(end)
            #perform dfs on the destination of the current destination: 
            if dfs(end, visited, flightMap, result, n):
                return True
        
            visited[starting][index] = 0
            result.pop()
    return False




#Main function to run the program
def main():
    print("TESTING RECONSTRUCT ITINERY...")
    input_01 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    input_02 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(findItinerary(input_01))
    print(findItinerary(input_02))
    print("END OF TESTING...")
main()