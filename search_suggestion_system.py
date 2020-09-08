import collections 
"""
https://leetcode.com/problems/search-suggestions-system/


"""


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        prefix_dic  = collections.defaultdict(list)
        
        
        for product in products:
            for i in range(len(product)):
                prefix = product[:i+1]
                prefix_dic[prefix].append(product)
        
        output = []
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            if prefix in prefix_dic:
                prefix_dic[prefix].sort()
                output.append(prefix_dic[prefix][:3])
        return output
sol = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(sol.suggestedProducts(products, searchWord))
