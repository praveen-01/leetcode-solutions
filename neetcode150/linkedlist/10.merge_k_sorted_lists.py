# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return 
        def merge_list(list1,list2):
            ans = ListNode(-1)
            temp = ans
            while list1 and list2:
                if list1.val<=list2.val:
                    temp.next=list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next
            temp.next = list1 if list1 else list2
            return ans.next
        
        list1 = lists[0]
        for list_r in lists[1:]:
            list1 = merge_list(list1,list_r)
        return list1
        