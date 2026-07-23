class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [None]
        
        if nums:
            sorted_nums = sorted(nums, reverse=True)
            self.heap.append(sorted_nums[0])
            for i in range(1, len(sorted_nums)):
                self.add(sorted_nums[i], get_kth=False)
            # print('Init: ')
            # self.show(self.heap)

    def show(self, heap) -> None:
        h = '[ '
        for num in heap:
            h += str(num) + ', '
        print(h + ']')
        

    def pop(self, heap) -> int:
        if len(heap) < 2:
            return None
        res = heap[1]

        # Substitute first element with last element
        last = heap.pop()
        if len(heap) < 2:
            return last

        heap[1] = last

        # Percolate down
        i = 1
        while 2 * i < len(heap):
            # Swap with right
            if len(heap) > 2 * i + 1 \
                and heap[2 * i + 1] > heap[2 * i] \
                and heap[i] < heap[2 * i + 1]:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                i = 2 * i + 1
            # Swap with left
            elif heap[i] < heap[2 * i]:
                heap[i], heap[i * 2] = heap[2 * i], heap[i]
                i = 2 * i
            else:
                break

        return res

    def get_kth(self) -> int:
        # Pop k times
        tmp_heap = self.heap.copy()
        kth = tmp_heap[1]
        for i in range(self.k):
            kth = self.pop(tmp_heap)
            # print(f'Pop value: {kth}')
            # self.show(tmp_heap)

        return kth


    def add(self, val: int, get_kth = True) -> int:
        self.heap.append(val)
        
        if len(self.heap) == 2:
            return self.heap[1]

        # The value has been added to the last position
        # so now, percolate up
        i = len(self.heap) - 1
        while i > 1:
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
                i = i // 2
            else:
                break

        res = 0
        if get_kth:
            # print(f'Add {val}')
            # self.show(self.heap)
            res = self.get_kth()
        return res

        

        
