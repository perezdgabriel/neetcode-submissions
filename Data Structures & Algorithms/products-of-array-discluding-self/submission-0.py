class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        zcount = 0
        for n in nums:
            if n == 0: zcount += 1
            else: prod *= n

        if zcount > 1:
            return [0] * len(nums)

        for n in nums:
            if n == 0: res.append(prod)
            elif zcount: res.append(0)
            else: res.append(int(prod / n))

        return res
        