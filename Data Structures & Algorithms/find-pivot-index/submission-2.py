class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)

        def sub_sum(start: int, end: int) -> int:
            sumr = prefix[end]
            suml = prefix[start - 1] if start > 0 else 0
            return sumr - suml

        for i in range(0, len(nums)):
            sum_left = sub_sum(0, i - 1) if i > 0 else 0
            sum_right = sub_sum(i + 1, len(nums) - 1) if i < len(nums) - 1 else 0
            print(f'i: {i} - suml: {sum_left} - sumr: {sum_right}')
            if sum_right == sum_left:
                return i
        
        return -1