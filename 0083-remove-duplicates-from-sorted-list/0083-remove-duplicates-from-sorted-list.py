# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        if not head:
            return head
        pre = head
        cur = head.next
        
        while cur:
            while cur and cur.val == pre.val:
                cur = cur.next
            if cur:
                pre.next = cur
                pre = cur
                cur = cur.next
            else:
                pre.next = None
        return dummy.next
            
            