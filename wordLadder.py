#Python3 program to solve the word ladder problem using DFS

#Problem statement: 

'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''
from collections import defaultdict


#Breadth first search approach: 
'''
Preprocessed form of word: hot: h*t or ho* or *ht
'''
def ladderLength(beginWord, endWord, wordList):    
        #base case: 
        if endWord not in wordList or not endWord or not beginWord or not wordList: 
            return 0

        #since all the words have the same length: 
        L = len(beginWord)

        #initialize a dictionary that would store the preprocessed forms of all the word in the word list
        combonationDict = defaultdict(list)
        #Convert all the words from the wordlist into the preproceseed form
        for word in wordList:
            for i in range(L):
                combonationDict[word[:i] + "*" + word[i+1:]].append(word)

        #create a queue to store the current word
        queue = collections.deque([(beginWord, 1)])
        #create an visited array to check for any node that has been visited
        visited = {beginWord: True}

        while queue:
            currentWord, level = queue.popleft() 
            for i in range(L):
                preProcessedWord = currentWord[:i] + "*" + currentWord[i+1:]
                #match the current preProcessed word with all the other processed word in the dictionary
                for word in combonationDict[preProcessedWord]:
                    #if the current word in the dictionary made it to the end...
                    if word == endWord: 
                        return level + 1
                    #if the word we are looking has not yet been visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                combonationDict[preProcessedWord] = []

        return 0

            
                




#driver code to test the problem
def main():
    print("TESTING WORD LADDER PROBLEM...")
    # print(ladderLength("hit", "cot", ["hot", "cot", "dot" ]))
    print("END OF TESTING...")

main()



