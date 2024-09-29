class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        # """

        # col = set()
        # row = set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 0:
        #             col.add(j) 
        #             row.add(i)
                    
        # for i in row:
        #     matrix[i] = [0]*len(matrix[i])

        # for i in range(len(matrix)):
        #     for j in col:
        #         matrix[i][j] = 0  

        # return matrix
        col0 = 1  # To handle the first column separately
        
        # Step 1: Traverse the matrix and mark the first row & column accordingly
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # Mark i-th row
                    matrix[i][0] = 0
                    
                    # Mark j-th column
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # Step 2: Mark with 0 from (1, 1) to (n-1, m-1)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        # Step 3: Finally, mark the first row and column
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if col0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0


