class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        Input: 1->2->4, 1->3->4
        
        Output: 1->1->2->3->4->4
        
        https://leetcode.com/problems/merge-two-sorted-lists/
        """
        curr = dummy = ListNode(-1)
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        while l1:
            curr.next = ListNode(l1.val)
            l1 = l1.next
            curr = curr.next
            
        while l2:
            curr.next = ListNode(l2.val)
            l2 = l2.next
            curr = curr.next
            
            
         
        return dummy.next 