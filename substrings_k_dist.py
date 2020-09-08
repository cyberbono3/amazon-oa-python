"""

https://leetcode.com/discuss/interview-question/370157

Input: s = "pqpqs", k = 2

Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
    
     0    1   2   3   4
s = "p    q   p   q   s
       
i = 1  seen = {"p, "q}}



start = 0
seen = set()
count = 0
for end in range(len(s)):
    seen.add(s[end])
    if len(seen) == k:
        count += 1
    while len(seen) > k:
        seen.remove(s[start])
        start += 1
        
     
    


"""

import collections

class Solution:
    def subStringsWithKDistinctCharacters(self, s, k):
        #s = list(s)
        count = 0
        right, left = 0, 0
        hmap = collections.defaultdict(int)
        for x in s:
            hmap[x] += 1
        
            if len(hmap) < k:
                continue
            
            if len(hmap) > k:
                del hmap[s[right]]
                right += 1
                left = right
                
            while hmap[s[right]] > 1:
                hmap[s[right]] -= 1
                right +=1
            
            count += right-left+1
        return count
sol = Solution()
print(sol.subStringsWithKDistinctCharacters('pqpqs', 2))

        
    