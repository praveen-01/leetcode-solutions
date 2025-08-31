# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        level = [root]
        while level:
            s = len(level)
            temp = []
            for i in range(s):
                cur_node = level.pop(0)
                if cur_node.left:
                    level.append(cur_node.left)
                if cur_node.right:
                    level.append(cur_node.right)
                temp.append(cur_node.val)
            res.append(temp[:])
        return res
        