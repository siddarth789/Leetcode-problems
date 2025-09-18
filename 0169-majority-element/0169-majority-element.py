class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        vote = 0 
        candidate=0
        
        for num in nums:
            if vote == 0:
                candidate = num
            
            if candidate == num:
                vote += 1
            else:
                vote -= 1
        
        return candidate
        