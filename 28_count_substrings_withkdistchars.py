"""
https://leetcode.com/problems/subarrays-with-k-different-integers/

Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Brutforce approach  O(n**3)
    n = len(A)
        
    count = 0
    for i in range(n):
        sub_arr = []
        for j in range(i, n):
            sub_arr += [A[j]]
            if len(set(sub_arr)) == K:
                count += 1
    return count
----------------------------------------------------------------------

O(n**2) approach


O(N**2) approach 
n = len(A)
count = 0
for i in range(n):
    dic = {}
    for j in range(i, n):
        dic[A[j]] = dic.get(A[j], 0) + 1
        if len(dic) == K:
            count += 1
return count 
                    


---------------------------------------------------------------------------









"""
class Solution:
    def subarraysWithKDistinct(self, A, K):
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                # remove the distinct at start_k, move start_k, start
                del freq[A[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                # update start_k and res (Notice: K >= 1)
                while freq[A[start_k]] > 1:
                    freq[A[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
                print(start, start_k, res)
        return res
sol = Solution()
print(sol.subarraysWithKDistinct("pqpqs", 2) == 7)
print(sol.subarraysWithKDistinct("aabab", 3) == 0)


