# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        slow = head

        while slow:
            values.append(slow.val)
            slow = slow.next

        max_twin = float('-inf')
        l, r = 0, len(values) - 1
        
        while l < r:
            max_twin = max(max_twin, values[l] + values[r])
            l += 1
            r -= 1
        
        return max_twin