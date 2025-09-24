# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        count = 0
        res = ListNode()
        temp = res
        total = 0
        while l1 or l2:
            total = 0
            if l1:
                total+=l1.val
                l1 = l1.next
            if l2:
                total+=l2.val
                l2 = l2.next
            total+=count
            node = ListNode(total%10)
            count = total//10
            temp.next = node
            temp = temp.next
        if count>0:
            temp.next = ListNode(count)
        return res.next