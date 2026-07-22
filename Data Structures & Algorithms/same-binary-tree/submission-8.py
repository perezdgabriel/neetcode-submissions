from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:    
        # if (not p and q) or (not q and p):
        #     return False
        qp = deque()
        if p: qp.append(p)
        qq = deque()
        if q: qq.append(q)

        if len(qp) != len(qq):
            return False
            
        while qp and qq:
            ll_p = len(qp)
            ll_q = len(qq)
            if ll_p != ll_q:
                return False

            for _ in range(ll_p):
                rp = qp.popleft()
                rq = qq.popleft()
                if rp:
                    qp.append(rp.right)
                    qp.append(rp.left)
                if rq:
                    qq.append(rq.right)
                    qq.append(rq.left)
                if (not rp and rq) or (not rq and rp):
                    return False
                if rp and rq and rp.val != rq.val:
                    return False
        
        return True