# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            if not head:
                return head
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second_head = slow.next
        slow.next = None
        reversed_head = reverse(second_head)
        temp = head
        while temp and reversed_head:
            temp1 = temp.next
            temp.next = reversed_head
            temp2 = reversed_head.next
            reversed_head.next = temp1
            temp = temp1
            reversed_head = temp2