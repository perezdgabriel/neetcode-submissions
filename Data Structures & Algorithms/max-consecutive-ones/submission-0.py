class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        local_result = 0
        for i, num in enumerate(nums, 1):
            if num == 1:
                local_result += 1
            else:
                result = max(result, local_result)
                local_result = 0
        
        return max(local_result, result)
        