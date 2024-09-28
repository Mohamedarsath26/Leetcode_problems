class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        # """

        col = set()
        row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    col.add(j) 
                    row.add(i)
                    
        for i in row:
            matrix[i] = [0]*len(matrix[i])

        for i in range(len(matrix)):
            for j in col:
                matrix[i][j] = 0  

        return matrix

        # rows_to_zero = set()
        # cols_to_zero = set()

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 0:
        #             rows_to_zero.add(i)  
        #             cols_to_zero.add(j) 

        
        # for i in rows_to_zero:
        #     matrix[i] = [0] * len(matrix[i])

        
        # for i in range(len(matrix)):
        #     for j in cols_to_zero:
        #         matrix[i][j] = 0

        # return matrix

