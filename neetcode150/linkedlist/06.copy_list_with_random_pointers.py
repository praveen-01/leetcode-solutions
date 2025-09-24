
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        temp = head
        d = {None:None}
        while temp:
            d[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            curr = d[temp]
            curr.next = d[temp.next]
            curr.random = d[temp.random]
            temp = temp.next
        return d[head]
