# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
An inorder traversal of bst would traverse the array in sorted order so we can have a counter and increase as we see a new node
when the counter reaches to k the current root is the kth smallest integer
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        count = 0
        def inorder(root):
            nonlocal ans,count
            if not root or ans:
                return
            inorder(root.left)
            count+=1
            if count==k:
                ans = root.val
                return
            inorder(root.right)
        inorder(root)
        return ans
        