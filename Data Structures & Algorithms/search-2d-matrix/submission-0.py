class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, ROWS * COLS - 1 

        while L <= R:
            middle = L + (R - L) // 2
            if matrix[middle // COLS] [middle % COLS] > target:
                R = middle - 1
            elif matrix[middle // COLS] [middle % COLS] < target:
                L = middle + 1
            else:
                return True

        return False