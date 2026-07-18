from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {num: index for index, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = ht.get(target - num, -1)
            if complement >= 0 and complement != i:
                return [i, complement]
        return []
