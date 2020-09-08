"""

https://leetcode.com/problems/reorder-data-in-log-files/


"""

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits 
       
        
        
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
print(sol.reorderLogFiles(logs))
