class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False

        for i in range(0,len(goal)):
            
            rotated = s[i:] + s[:i]

            if rotated == goal:
                return True
        
        return False
        
        





        
        