from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 1
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]

        return [left, right]
