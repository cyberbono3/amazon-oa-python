# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def match(s, t):
            if not (s and t):
                return False
            elif not s and not t:
                return True
            equality = s.val == t.val
            left = self.isSubtree(s.left, t.left) 
            right = self.isSubtree(s.right, t.right)
            return equality and left and right
           
        if not s and not t:
            return True
        if not (s and t):
            return False
        stack = [s]
        while stack:
            curr = stack.pop()
            if curr.val == t.val:
                return match(curr, t)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        