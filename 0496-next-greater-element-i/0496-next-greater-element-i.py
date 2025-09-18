class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        stack=[]
        for cur in nums2:
            while stack and stack[-1]<cur:
                ele=stack.pop()
                d[ele]=cur
            stack.append(cur)
        while stack :
             d[stack.pop()]=-1
        res=[]
        for i in nums1:
            res.append(d[i])
        return res
