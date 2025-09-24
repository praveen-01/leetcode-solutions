# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        def reverse(node):
            tail = node
            curr = node
            prev = None    
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev,tail
        if not head or not head.next:
            return head
        count = 1
        start = head
        end = head
        ans = None
        flag = False
        prev_end = None
        while end:
            while count<k and end:
                end = end.next
                count+=1
            if not end:
                break
            if count==k:
                temp = end.next
                end.next = None
                reverse_head,reversed_tail = reverse(start)
                if not prev_end:
                    prev_end = reversed_tail
                else:
                    prev_end.next = reverse_head
                    prev_end = reversed_tail
                if not flag:
                    ans = reverse_head
                    flag = True
                reversed_tail.next = temp
                start = temp
                end = temp
                count = 1
        return ans
