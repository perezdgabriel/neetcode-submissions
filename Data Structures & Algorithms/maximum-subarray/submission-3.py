class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        if len(nums) == 1: 
            return nums[0]

        for i in range(len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum