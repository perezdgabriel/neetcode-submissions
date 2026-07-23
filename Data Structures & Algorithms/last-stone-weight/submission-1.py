import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        heapq.heapify_max(self.heap)

        while len(self.heap) > 1:
            el1, el2 = heapq.heappop_max(self.heap), heapq.heappop_max(self.heap)
            if el1 - el2 != 0:
                heapq.heappush_max(self.heap, abs(el1 - el2))
            
        
        return heapq.heappop_max(self.heap) if self.heap else 0
    