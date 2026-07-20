# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode], output: List[int]) -> List[int]:
            if not root:
                return
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        o = []
        self.inorder(root, o)
        return o

        