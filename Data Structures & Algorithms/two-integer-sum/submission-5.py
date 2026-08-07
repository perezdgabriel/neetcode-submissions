class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for index, num in enumerate(nums):
            if num in ht:
                return [ht[num], index]
            ht[target - num] = index
        
        return [-1, -1]
