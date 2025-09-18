class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m=0
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if i+1 in d and d[i]+d[i+1]>m:
                m=d[i]+d[i+1]
        return m

        