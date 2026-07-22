from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        curr = root
        q = deque()
        q.append(curr)
        while q:
            level_len = len(q)
            for _ in range(level_len):
                curr = q.popleft()
                curr.left, curr.right = curr.right, curr.left
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return root
        
