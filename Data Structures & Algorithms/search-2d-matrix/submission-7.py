class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        rl, rr = 0, rows - 1
        while rl <= rr:
            rmid = (rl + rr) // 2
            if target < matrix[rmid][0]:
                rr = rmid - 1
            elif target > matrix[rmid][cols - 1]:
                rl = rmid + 1
            else:
                cl = 0
                cr = cols - 1
                while cl <= cr:
                    cmid = (cl + cr) // 2
                    if target > matrix[rmid][cmid]:
                        cl = cmid + 1
                    elif target < matrix[rmid][cmid]:
                        cr = cmid - 1
                    else:
                        return True
                return False
        
        return False
