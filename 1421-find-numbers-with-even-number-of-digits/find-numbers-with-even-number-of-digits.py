class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in range(len(nums)):
            digit = len(str(nums[i]))
            
            if digit % 2 == 0:
                count+=1
        return count
        