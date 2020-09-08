class Solution(object):
    # 
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        
                             e s           e s
        S = "a b a b c b a c a d e f e g d e h i j h k l i j"
        
        https://leetcode.com/problems/partition-labels/
        
        """
        rightmost = {c:i for i,c in enumerate(S)}
        left, right = 0, 0
        result = []
        for i, letter in enumerate(S):
            right = max(right,rightmost[letter])
            if i == right:
                result.append(right - left + 1)
                left = i+1
        return result
s = Solution()
S = "ababcbacadefegdehijhklij"
print(s.partitionLabels(S) == [9,7,8])