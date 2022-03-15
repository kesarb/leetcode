"""
692. Top K Frequent Words
Medium

4194

240

Add to List

Share
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for i in words:
            dic[i] = dic.get(i, 0) - 1
        heap = [(val,i) for i, val in dic.items()]
        heapq.heapify(heap)
        i = k
        
        res = []
        while i > 0:
            res.append(heapq.heappop(heap)[1])
            i-=1
        return res
        
    def topKFrequent_bucket(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for i in words:
            dic[i] = dic.get(i, 0) + 1
            
        res = [[] for i in range(len(words)+1)]
        
        for i, val in dic.items():
            res[val].append(i)
            
        i = len(words)
        output = []
        while i > 0:
            if res[i]:
                res[i].sort()
                for j in res[i]:
                    output.append(j)
                    if len(output) == k:
                        return output
            i -= 1
