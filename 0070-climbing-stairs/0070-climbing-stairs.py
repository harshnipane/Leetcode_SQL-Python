class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 2  
        prev2 = 1  
        if n ==1:
            return 1
        for _ in range(3, n + 1):
            dp = prev1 + prev2
            prev2 = prev1
            prev1 = dp
            print("dp= " ,dp, "prev1 =",prev1,"prev2 =",prev2)
        return prev1
    