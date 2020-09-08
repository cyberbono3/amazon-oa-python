"""
https://leetcode.com/problems/copy-list-with-random-pointer/






"""


class Node:
    def __init__(self, val, random = None, next = None, ):
        self.val = val
        self.next = next
        sel.random = random
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, node):
        curr = self.head
        while curr :
            curr = curr.next
        curr = node
                
    
        
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
sol = Solution()
list = LinkedList:
    
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
for val, random_index in head:
    
print(sol.copyRandomList(head) == [[7,None],[13,0],[11,4],[10,2],[1,0]])

"""
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,None],[3,0],[3,None]]
Output: [[3,None],[3,0],[3,None]]
"""


                                      
        