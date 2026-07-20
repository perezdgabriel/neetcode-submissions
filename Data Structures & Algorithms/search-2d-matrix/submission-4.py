class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix[0]) == 0:
            return False

        up, down = 0, len(matrix) - 1
        row = []
        while up <= down:
            if len(matrix) == 1:
                row = matrix[0]
            else:
                mid = (up + down) // 2
                if target > matrix[mid][0]:
                    if target <= matrix[mid][-1]:
                        row = matrix[mid]
                    else:
                        up = mid + 1
                elif target < matrix[mid][0]:
                    down = mid - 1
                else:
                    return True

            print(row)
            if row:
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target < row[mid]:
                        right = mid - 1
                    elif target > row[mid]:
                        left = mid + 1
                    else:
                        return True
                return False
        return False
                    
                