# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True

'''
can we make use of bst property that root is always greater than left and less than right?
check if root 
everytime we check if current node is in between valid ranges, for left subtree the range gets updated with max as each left child should be less than its parent and similaryly for right
the min gets changed with parent as it has to be greater than parent
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,mini,maxi):
            if not root:
                return True
            if root.val<=mini or root.val>=maxi:
                return False
            return valid(root.left,mini,root.val) and valid(root.right,root.val,maxi)
        return valid(root,float("-inf"),float("inf"))