class Solution:
    def mySqrt(self, x: int) -> int:
        from math import ceil
        
        l = len(str(x))
        out = int('1' + '0' * (ceil(l/2) - 1))
        
        while ((out * out) < x):
            out += 1
            
        if ((out * out) > x):
            out -= 1
            
        return(out)
        
        