'''
Do a preorder traversal and check the maxi with current val if maxi is <= curr then we have a good node so increase the count
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def traverse_paths(root,maxi):
            if not root:
                return
            nonlocal count
            if maxi<=root.val:
                count+=1
                maxi = root.val
            traverse_paths(root.left,maxi)
            traverse_paths(root.right,maxi)
        traverse_paths(root,root.val)
        return count