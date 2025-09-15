class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1=sum(nums)
        sum2=0
        for i in nums:
            while i:
                sum2+=i%10
                i//=10
        return abs(sum1-sum2)



        