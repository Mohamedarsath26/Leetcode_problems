class Solution:
    def conversion(self,ind1D,col):
        r = ind1D//col
        c = ind1D%col
        return r,c

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        low = 0
        high = (row*col) - 1

        while(low<=high):
            mid = (low+high)//2

            r,c = self.conversion(mid,col)

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

            





        