from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p = sorted(piles)
        l, r = 1, p[-1]
        result = p[-1]
        while l <= r:
            mid = (l + r) // 2
            in_time = self.in_time(mid, p, h)
            if in_time:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result


    def in_time(self, k: int, piles: List[int], h:int) -> bool: 
        return sum(ceil(bananas / k) for bananas in piles) <= h



    