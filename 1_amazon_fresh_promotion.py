
# https://leetcode.com/discuss/interview-question/762546/

class Solution:
    def is_winner(self, codeList, shoppingCart ):
        # address edge cases
        if not codeList :
            return 1
        if not shoppingCart:
            return 0
        
        newCodeList = []
        for l in codeList:
            newCodeList.extend([f for f in l])
            
        first_match = False
        i, j = 0, 0
        while i < len(newCodeList) and j < len(shoppingCart):
            match = newCodeList[i] == shoppingCart[j] or newCodeList[i] == 'anything'
            if not first_match :
                if match:
                    first_match = True
                    j += 1
                    i += 1
                    continue
                j += 1
            else:
                if not match:
                    break
                j += 1
                i += 1
                    
    
        return i == len(newCodeList)  

 
sol = Solution()        
codeList1 =  [["apple", "apple"], ["banana", "anything", "banana"]] 
shoppingCart1 = ["orange", "apple", "apple", "banana", "orange", "banana"]
print(sol.is_winner(codeList1, shoppingCart1))
#True

codeList2 = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart2 = ["banana", "orange", "banana", "apple", "apple"]
print(sol.is_winner(codeList2, shoppingCart2))
#False    
        
codeList3 = [["apple", "apple"], ["banana", "anything", "banana"]] 
shoppingCart3 = ["apple", "banana", "apple", "banana", "orange", "banana"]
print(sol.is_winner(codeList3, shoppingCart3))
#False
        
codeList4 = [["apple", "apple"], ["apple", "apple", "banana"]] 
shoppingCart4 = ["apple", "apple", "apple", "banana"]
print(sol.is_winner(codeList4, shoppingCart4))
#False
        

    
    
    




