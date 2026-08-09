class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums).most_common(1)
        return c[0][0]