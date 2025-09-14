class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def sum_of_digits(n):
            s=0
            while n:
                d=n%10
                s+=d
                n=n//10
            return s
        def product_of_digits(n):
            p=1
            while n:
                d=n%10
                p*=d
                n=n//10
            return p
        return product_of_digits(n)-sum_of_digits(n)