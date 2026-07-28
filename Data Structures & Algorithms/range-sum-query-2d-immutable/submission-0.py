class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in matrix:
            row_sum = []
            row_total = 0
            for col in row:
                row_total += col
                row_sum.append(row_total)
            self.prefix.append(row_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            sumr = self.prefix[i][col2]
            suml = self.prefix[i][col1 - 1] if col1 > 0 else 0
            total = total + (sumr - suml)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)