class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            ans.append(self.variation_2(i))
        return ans

    def variation_2(self,n):
        ans = 1
        ansRow = [1]
        for i in range(1,n):
            ans = ans*(n-i)
            ans = ans//i
            ansRow.append(ans)
        return ansRow

        
                
            