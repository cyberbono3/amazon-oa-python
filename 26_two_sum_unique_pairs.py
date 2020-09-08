"""

Input: nums = [1, 1, 2, 45, 46, 46], target = 47

1, 1



"""

class Solution:
    def unique_pairs(self, nums, target):
        s = set()
        dic = {}
        for i,x in enumerate(nums):
            if target - x in s:
                dic[target-x] = x
            else:
                s.add(x)
        print(dic)
        return len(dic)
sol = Solution()
print(sol.unique_pairs([1, 1, 2, 45, 46, 46], 47))