# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        level = [root]
        while level:
            s = len(level)
            temp = -101
            for i in range(s):
                node = level.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                temp = node.val
            if temp!=-101:
                res.append(temp)
        return res
        