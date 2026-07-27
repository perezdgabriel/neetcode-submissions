class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        li = 0
        total = 0
        res = float('inf')

        for ri, num in enumerate(nums):
            total += num
            while total >= target:
                res = min(res, ri - li + 1)
                total -= nums[li]
                li += 1
        
        return 0 if res == float('inf') else res