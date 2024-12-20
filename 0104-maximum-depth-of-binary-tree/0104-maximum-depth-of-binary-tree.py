# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        max_depth = 0
        if root: stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if node.left: stack.append((node.left, depth+1))
            if node.right: stack.append((node.right, depth+1))
        return max_depth
        

        # TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: None, right: None}}