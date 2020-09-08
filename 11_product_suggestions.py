import collections 

# https://leetcode.com/problems/search-suggestions-system/

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
                suggested = sorted(prefix_dic[prefix])[:3]
                output.append(suggested)
        return output
    
s = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(s.suggestedProducts(products, searchWord) == [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
])

products = ["havana"]
searchWord = "havana"
print(s.suggestedProducts(products, searchWord) == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]])


