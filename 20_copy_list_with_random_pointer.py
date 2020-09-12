"""
https://leetcode.com/problems/copy-list-with-random-pointer/

"""

import unittest

class Node:
    def __init__(self, val, random = None, next = None, ):
        self.val = val
        self.next = next
        sel.random = random
            
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 1st pass clone all nodes to the mapping 
        dic = {}
        if not head:
            return None
        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        # second pass fill in next and random pointers 
        curr = head
        while curr:
            dic[curr].next = dic.get(curr.next)
            dic[curr].random = dic.get(curr.random)
            curr = curr.next
        return dic[head]





                                      
        