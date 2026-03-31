class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s = s.lstrip()
        sign = 1
        i = 0
        if not s :
            return 0 
        
        if s[i]== '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        num = 0 
        while i < len(s) and s[i].isdigit():
            dig = int(s[i])

            if num >(INT_MAX - dig) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + dig
            i += 1
        return sign * num



            
        