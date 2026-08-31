class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[list[int]]:
        l, r = 0, len(nums) - 1
        sums = []
        while l < r:
            res = nums[l] + nums[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            else:
                sums.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
        
        return sums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        triplets = []
        i = 0
        for i in range(len(nums) - 2):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue

            tsum = self.twoSum(s_nums[i + 1:], -s_nums[i])
            print(tsum)
            for a, b in tsum:
                triplets.append([s_nums[i], a, b])
            
            
        return triplets




        