""" Throttling Gateway
Non-Critical requests for a transaction system are routed through a throttling 
gateway to ensure that the network is not choked by non-essential requests.
The gateway has limits as follows:
1. The number of transactions in any given second cannot exceed 3.
2. The number of transactions in any given 10 second period cannot exceed 20. A
   10 seconds period would count all transactions arriving from any time T to
   T + 9 (inclusive of both) for any valid time T.
3. The number of transaction in any given minute cannot exceed 60 (similar to 
   above, 1 minutes is from T to T + 59)
Any request that exceeds any of the above limits will be dropped by the gateway
Given the times at which different requests arrive (sorted in ascending order of 
arrivals), find how many of them will be dropped.
Note: Even if a request is dropped it is till considered for future calculations.
Author: Weikun Han <weikunhan@g.ucla.edu>
Reference: https://www.1point3acres.com/bbs/thread-610975-1-1.html
Time complexity: O(n^2)
Space complexity: O(n)
Input: 
n = 22
requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 11, 11, 11]
Output: 
1
Explanation:
There are total 22 requset. 19 requset within 10 sec which no need to drop.
There are four requests in the first secound. One of them will be dropped as 4 > 3
"""
def droppedRequests(requestTime):
    # Write your code here
    res = 0
    sec_10 = []
    min_window = []
    secctr = 0

    for idx, each in enumerate(requestTime):

        if idx > 0 and each == requestTime[idx - 1]:
            secctr += 1
        else:
            secctr = 1

        while sec_10 and each - 10 > sec_10[0]:
            sec_10.pop(0)
        while min_window and each - 60 > min_window[0]:
            min_window.pop(0)

        if secctr > 3 or len(sec_10) + 1 > 20 or len(min_window) + 1 > 60:
            res += 1
        sec_10.append(each)
        min_window.append(each)

    print(res)

droppedRequests([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 11, 11, 11])

