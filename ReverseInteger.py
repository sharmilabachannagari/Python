class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = 0
        
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10
            
            # Check overflow before multiplying by 10
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num
