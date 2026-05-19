class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums_copy = nums.copy()
        for i in range(size):
            nums_copy.append(nums[i])
        return nums_copy
        
        