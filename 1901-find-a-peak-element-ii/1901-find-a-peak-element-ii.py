class Solution:
    ## finding maximum element indexes in column
    def max_col_ele(self,mat,n,m,mid):
        max_ind = 0
        maxi = -1
        for i in range(n):
            if mat[i][mid] > maxi:
                max_ind = i
                maxi = mat[i][mid]
        return max_ind 

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m-1
        while(low<=high):
            mid = (low+high)//2
            row = self.max_col_ele(mat,n,m,mid)

            ##check on left and right

            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            elif mat[row][mid] < left:
                high = mid -1
            else:
                low = mid + 1

        return [-1,-1]

        
        