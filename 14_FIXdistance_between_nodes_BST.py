


#  Build BST

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class BST:
    def __init__(self, root = None):
        self.root = root 
    
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val < self.root.val:
            root.left = self.insert(root.left, val)
        elif val > self.root.val:
            root.right = insert(root.right, val) 
        
        return root


    def LCA(self, root, p, q):
        parent_val = root.val

        if p < parent_val and q < parent_val:
            return lowestCommonAncestor(root.left, p, q)

        if p > parent_val and q > parent_val:
            return lowestCommonAncestor(root.right, p, q)

        return root
    

    def height(self, node, val):
        if node.val == val:
            return 0
        elif val < node.val:
            return 1 + height(node.left, val)
        else:
            return 1 + height(node.right, val)

class Solution:
    def compute_distance_between_nodes(self, vals, p, q):
        bst = BST()
        for v in vals:
            bst.insert(bst.root, v)
        lca = bst.LCA(bst.root, p, q)
        h1 = bst.height(lca, p)
        h2 = bst.height(lca, q)
        return h1 + h2

sol = Solution()
vals = [4, 2, 7, 1, 3, 5]
p, q = 1, 2
print(sol.compute_distance_between_nodes(vals, p, q))
