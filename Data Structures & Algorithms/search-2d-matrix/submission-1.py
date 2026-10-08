class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = 0
        row_end = len(matrix)
        column_start = 0
        column_end = len(matrix[0])
        row_mid = (row_start + row_end) // 2
        column_mid = (column_start + column_end) // 2

        # Row (logm)
        while row_end-row_start > 1:
            if matrix[row_mid][0] < target:
                row_start = row_mid
                row_mid = (row_start + row_end) // 2
            elif matrix[row_mid][0] > target:
                row_end = row_mid
                row_mid = (row_start + row_end) // 2
            elif matrix[row_mid][0] == target:
                return True
        # Column (logn)
        while column_end-column_start > 1:
            if matrix[row_mid][column_mid] < target:
                column_start = column_mid
                column_mid = (column_start + column_end) // 2
            elif matrix[row_mid][column_mid] > target:
                column_end = column_mid
                column_mid = (column_start + column_end) // 2
            elif matrix[row_mid][column_mid] == target:
                return True

        # logm + logn = log(m*n)
        return matrix[row_mid][column_mid] == target
