# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverse(head):
            pre = None
            
            while head:
                next = head.next
                head.next = pre
                pre = head
                head = next
            
            return pre
        
        dummy = ListNode(-1)
        dummy.next = reverse(head)
        cur = dummy.next
        carry = 1
        
        while cur:
            carry += cur.val
            cur.val = carry % 10
            carry //= 10
            if not cur.next and carry:
                cur.next = ListNode(1)
                break
            cur = cur.next
            
        
        return reverse(dummy.next)
        
        