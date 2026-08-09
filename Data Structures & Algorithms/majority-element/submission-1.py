class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums[0]
        count = 0
        for num in nums:
            if num == cur:
                count += 1
                if count >= len(nums) / 2:
                    return num
            else:
                count = 1
                cur = num