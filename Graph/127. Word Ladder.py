"""
127. Word Ladder
Hard

7636

1626

Add to List

Share
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #search for desitination if it is not there rettun 0
        #take word list and make set
        #visit array for visiting each word list repeating or not
        #push initial word(begin) along with distence(1) and continue to expolre the possible one letter change word and push into the queue if it is not visited yet
        #while poping the word look for whether its a Destination or not
        # if yes return the distence of it 
        
        d = set(wordList)
        d.add(beginWord)
        if endWord not in d:
            return 0
        
        visit = set()
        visit.add(beginWord)
        queue = [(beginWord, 1)]
        
        while queue:
            qword, l = queue.pop(0)
            if qword == endWord:
                return l
            
            for i in range(len(qword)):
                for j in range(27):
                    new_word = qword[:i]+chr(ord('a')+j)+qword[i+1:]
                    if new_word not in visit and new_word in d:
                        visit.add(new_word)
                        queue.append((new_word, l+1))
                        
        return 0
    
                
            
            
