
"""
              20
             /    \
            12       18
         /  | \     /  \ 
        11  2  3    15  8
(11, 1)  (2,1) (3,1)

"""

class TreeNode:
    def __init__(self, value, children = []):
        self.val = value
        self.children = children
        
class Solution:
    def __init__(self):
        self.average_max = float('-inf')
        self.average_node = None
    
    def compute_max_average_sum(self, root):
        if not root or not root.children :
            return None    
        self.dfs(root) 
        return self.average_node.val
        
    def dfs(self, node):
        # if node is None
        if not node:
            return (0, 0)
        
        temp_sum, temp_num = node.val, 1
        for child in node.children:
            child_sum, child_num = self.dfs(child)
            temp_sum += child_sum
            temp_num += child_num
        
        average = temp_sum / temp_num 
        if temp_num > 1 and average > self.average_max:
            self.average_max = average
            self.average_node = node
        
        return (temp_sum, temp_num)

sol = Solution()          
n4 = TreeNode(11)
n5 = TreeNode(2)
n6 = TreeNode(3)
n7 = TreeNode(15)
n8 = TreeNode(8)
n2 = TreeNode(12, [n4, n5, n6])
n3 = TreeNode(18, [n7, n8])
n1 = TreeNode(20, [n2, n3])
print(sol.compute_max_average_sum(n1)) 



    

