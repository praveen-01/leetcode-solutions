# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        count = 0
        while count<n:
            fast = fast.next
            count+=1
        slow = head
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        if slow==head:
            return head.next
        if prev:
            prev.next = slow.next
        return head
        