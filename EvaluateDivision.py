#Problem 399. Evaluate Division

'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

'''
from collections import defaultdict
def calcEquation(equations, values, queries):
	"""
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
	variableAndValue = defaultdict(set)
	result = []
	#create a hash map to store all the numerator and denominators of the 
	#equations and its values
	for i in range(len(equations)):
		value = values[i]
		variableAndValue[equations[i][0]].add((equations[i][1], value))
		variableAndValue[equations[i][1]].add((equations[i][0], 1/value))
	
	#helper method to calculate each query expression by traversing the 
	#hash map:
	def findPath(start, end, current, visited):
		#base case: we cannnot calculate the expression because both the start and end are not in the hashmap
		if start not in variableAndValue or end not in variableAndValue:
			return -1.0 
		#if start and end are the same, that means we have found the result for the current expression
		if start == end: 
			return current 
		visited.add(start)
		#go through the array values of the start node and check for its values
		for node in variableAndValue[start]:
			if node[0] not in visited:
				retVal = findPath(node[0], end, current * node[1], visited)
				if retVal != -1.0:
					return retVal
		return -1.0

	#loop through the query to and find its values
	for query in queries:
		#pass the query into the helper method that calcu;ate each of its expression
		res = findPath(query[0], query[1], 1, set())
		result.append(res)
	return result



#Main function to run the test case: 
def main():
	print("TESTING EVALUATE DIVISION... ")

	equations = [["a","b"],["b","c"]]
	values = [2.0,3.0]
	queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
	print(calcEquation(equations, values, queries))
	
	equations = [["a","b"],["b","c"],["bc","cd"]]
	values = [1.5,2.5,5.0]
	queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

	print(calcEquation(equations, values, queries))
	
	equations = [["a","b"]]
	values = [0.5]
	queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

	print(calcEquation(equations, values, queries))
	print("END OF TESTING...")

main()
