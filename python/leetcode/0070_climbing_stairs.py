"""
This is a classic fibonacci number problem

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        res  = [0]*(n+1)
        res[1] = 1
        res[2] = 2
        
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2]
        
        return res[n]
