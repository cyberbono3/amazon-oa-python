
"""

Build BST construct binary tree from preorder traversal 
Find LCA
Find Distance from LCA to given points


"""




class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
cass Solution:
    def build_tree_from_preorder(self, preorder, index = 0):
        """
        preorder [2, 1 ,3]
        
                 0  1  2
        inorder [1, 2, 3]
        inorder_dic = {x:i for i,x in enumerate(inorder)}
        
        
        """
        def build_tree(left, right):
            if left > right or self.pre_index > len(preorder) - 1:
                return None
            
            val = preorder[self.pre_index]
            root = TreeNode(val)
            self.pre_index += 1
            
            in_index = inorder_dic[val]
            root.left = build_tree(left, in_index - 1)
            root.right = build_tree(in_index + 1, right)
            
            return root
           
            
            
        inorder = sorted(preorder)
        self.pre_index = 0
        inorder_dic = {x:i for i,x in enumerate(inorder)}
        return build_tree(0, len(preorder)-1)
    
        def find_LCA(self, root, node1, node2):
            
            
        def find_distance
            
            
            
       


    root = 
    
        

preorder = [2,1,3]
node1 = 1
node2 = 3


        
