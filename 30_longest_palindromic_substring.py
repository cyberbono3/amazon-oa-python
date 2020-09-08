class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        
        
        """
        def expand_from_center(left, right):
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else: break
            return (left + 1, right - 1)
        
        
        if not s:
            return ""
        n = len(s)
        if n == 1:
            return s[0]
        res = (float("-inf"), 0, 0)
        for i in range(1, n):
            l1, r1 = expand_from_center(i, i)
            l2, r2 = expand_from_center(i-1, i)
            ln1, ln2 = r1 - l1 + 1, r2 - l2 + 1
            if ln1 >= ln2 and ln1 > res[0]:
                res = (ln1, l1, r1)
            elif ln2 > ln1 and ln2 > res[0]:
                res = (ln2, l2, r2)
        return "" if res[0] == float("-inf") else s[res[1]:res[2]+1]
