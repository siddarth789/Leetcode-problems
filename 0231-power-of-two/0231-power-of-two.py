class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        while n:
            if n==1:
                return True
            elif n%2!=0:
                return False
            else:
                n=n//2
       

        