class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            total_sum += n
        
        sum_left = 0
        for i, num in enumerate(nums):
            sum_right = total_sum - sum_left - num
            if sum_left == sum_right:
                return i
            sum_left += num
        
        return -1