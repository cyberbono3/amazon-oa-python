"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.


Example 1:
               0   1  2    3   4
Input: nums = [1, 10, 25, 35, 60], target = 60
Output: [2, 3]            25

dic = {}
for i,x in enumerate(arr):
    if target - x in dic:
        return [i, dic[target-x]]
    dic[x] = i
        
"""

class Solution:
    def two_sum_problem(self, arr, target):
        target -= 30
        dic = {}
        res = []
        for i,x in enumerate(arr):
            if target - x in dic:
                res.append([target-x, x])
            dic[x] = i
        res.sort()
        x, y = res.pop()
        return [dic[x], dic[y]]   
        
            

sol = Solution()
print(sol.two_sum_problem([1, 10, 25, 35, 60], 90))
print(sol.two_sum_problem([20, 50, 40, 25, 30, 10], 90))

        