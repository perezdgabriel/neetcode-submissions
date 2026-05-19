class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader, writer = 0, 0
        for num in nums:
            if num != val:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1

        return writer