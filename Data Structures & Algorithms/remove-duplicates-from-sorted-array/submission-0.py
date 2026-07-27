class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        char_set = set()
        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            if num in char_set:
                nums.remove(num)
            else:
                char_set.add(num)
                i += 1

            # print(f'char_set: {char_set} - nums:{nums} - i:{i}')
        
        return len(nums)