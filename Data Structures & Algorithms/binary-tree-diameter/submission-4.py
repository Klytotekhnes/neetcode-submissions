# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diametrAndDepth(root):
            if not root:
                return 0, -1

            left_max_diametr, left_max_depth = diametrAndDepth(root.left)
            right_max_diametr, right_max_depth = diametrAndDepth(root.right)

            max_depth = max(left_max_depth, right_max_depth) + 1
            max_diametr = max(left_max_diametr, right_max_diametr, left_max_depth + right_max_depth + 2)

            return max_diametr, max_depth

        diametr, _ = diametrAndDepth(root)
        return diametr