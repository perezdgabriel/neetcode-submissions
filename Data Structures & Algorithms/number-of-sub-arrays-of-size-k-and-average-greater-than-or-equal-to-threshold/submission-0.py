class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        li = 0
        total = 0
        
        for ri, num in enumerate(arr):
            total += num
            if ri - li + 1 > k:
                total -= arr[li]
                li += 1

            if ri - li + 1 == k:
                # print(f'ri:{ri}, li:{li}, total:{total}')
                if total / k >= threshold:
                    res += 1

        return res