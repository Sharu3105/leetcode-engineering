class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign = 1
        idx = 0
        
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                sign = -1
            idx += 1

        result = 0
        
        while idx < len(s) and s[idx].isdigit():
            result = result * 10 + (ord(s[idx]) - ord('0'))
            idx += 1

        result = sign * result

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
