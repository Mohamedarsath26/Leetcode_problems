class Solution:
    def myAtoi(self, s: str) -> int:
        ##step 1

        s = s.lstrip()
        if not s:
            return 0

        ## sign

        sign = 1
        index = 0

        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        ## read num

        num = 0
        while index<len(s) and s[index].isdigit():
            num = num*10 + int(s[index])
            index+=1
        
        ##apply sign

        num *= sign

        ## within range

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num

