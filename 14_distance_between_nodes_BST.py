"""

       4
      / \
    2    7
   / \   / 
  1  3   5

vals = [4, 2, 7, 1, 3, 5]
p, q = 1, 2


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def constructBST(self, left, right, inorder):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(inorder[mid])
        root.left = self.constructBST(left, mid-1, inorder)
        root.right = self.constructBST(mid+1, right, inorder )
        return root

    def preorder(self, root):
        if not root: return []
        return [root.val] + preorder(root.left)  + preorder(root.right)
    
    def LCA(self, root, p, q):
        parent_val = root.val
        
        if p < parent_val and q < parent_val:
            return self.LCA(root.left, p, q)
       
        if p > parent_val and q > parent_val:
            return self.LCA(root.right, p, q)
        
        return root
    
    def height(self, node, val):
        if node.val == val:
            return 0
        elif val < node.val:
            return 1 + self.height(node.left, val)
        else:
            return 1 + self.height(node.right, val)

    def compute_distance_between_nodes(self, vals, p, q):
        inorder = sorted(vals)
        root = self.constructBST(0, len(inorder)-1, inorder)
        bst = self.preorder(root)
        print(bst)
        lca = self.LCA(root, p, q)
        h1 = self.height(lca, p)
        h2 = self.height(lca, q)
        return h1 + h2

sol = Solution()
vals = [4, 2, 7, 1, 3, 5]
p, q = 1, 2
print(sol.compute_distance_between_nodes(vals, p, q))





"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def insert(root, val):
    if root == None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

bst = []
def preorder(root):
    if root == None:
        bst.append(None)
        return
    bst.append(root.val)
    preorder(root.left)
    preorder(root.right)

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: int
    :type q: int
    :rtype: TreeNode
    """
    parent_val = root.val

    if p < parent_val and q < parent_val:
        return lowestCommonAncestor(root.left, p, q)

    if p > parent_val and q > parent_val:
        return lowestCommonAncestor(root.right, p, q)

    return root
        
def height(root, val):
    if root.val == val:
        return 0
    
    if val < root.val:
        return (height(root.left, val) + 1)
    else:
        return (height(root.right, val) + 1)

l = [4, 2, 7, 1, 3, 5]
p = 1
q = 2
root = None
for val in l:
    root = insert(root, val)
preorder(root)

print(bst)
lca = lowestCommonAncestor(root, p, q)
print(lca.val)
h1 = height(lca, p)
h2 = height(lca, q)
print(h1 + h2)



    

