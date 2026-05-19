class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0 for i in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        value = self.array[self.size - 1]
        self.size -= 1
        return value

    def resize(self) -> None:
        new_array = [0 for i in range(self.capacity * 2)]
        for i, value in enumerate(self.array):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity