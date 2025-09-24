class Solution:
    def climbStairs(self, n: int) -> int:
        prev1,prev2,curr=3,2,0
        if n<=3:
            return n
        for i in range(3,n):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return curr
        