class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []
        pre_prod, suf_prod = 1, 1
        zcount = 0
        r = len(nums) - 1
        for l, num in enumerate(nums):
            # prefix
            if num == 0:
                zcount += 1
                prefix.append(0)
            else:
                pre_prod *= num
                prefix.append(pre_prod)

            # suffix
            if nums[r] != 0: suf_prod *= nums[r]
            suffix.append(suf_prod)
            r -= 1

        if zcount > 1: return [0] * len(nums)
        suffix = suffix[::-1]
        print(f'prefix: {prefix} - suffix: {suffix}')
        for i, num in enumerate(nums):
            if num == 0: res.append(pre_prod)
            elif zcount: res.append(0)
            else:
                left = prefix[i - 1] if i > 0 else 1
                right = suffix[i + 1] if i < len(nums) - 1 else 1
                print(f'i: {i} - left: {left} - right: {right}')
                res.append(left * right)

        return res