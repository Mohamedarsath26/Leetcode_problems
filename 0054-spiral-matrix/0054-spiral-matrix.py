class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        n = len(matrix) #row
        m = len(matrix[0]) #col

        top = 0
        left = 0
        right = m-1 #column
        bottom = n-1#row
        ans = []
        while(top<=bottom and left<=right): ##check the condition 

            #left to right
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            
            #top to bottom
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            
            #checks if still column have or not
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            #checks if still row have or not
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans


        