"""
https://leetcode.com/problems/generate-parentheses/





"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        
       [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
        ]
    
        
        """
        if n == 1:
            return ['()']
        last_list = self.generateParenthesis(n-1)
        print(last_list)
        res = []
        for t in last_list:
            curr = t + ')'
            for index in range(len(curr)):
                if curr[index] == ")":
                    res += [curr[:index] + '(' + curr[index:]]
        return list(set(res))
            