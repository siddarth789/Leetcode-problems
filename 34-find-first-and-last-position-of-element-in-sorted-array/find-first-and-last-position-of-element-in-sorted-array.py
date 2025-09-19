class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        s,e=0,len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                res[0]=mid
                e=mid-1
            elif nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
        s,e=0,len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                res[1]=mid
                s=mid+1
            elif nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
        return res
            
