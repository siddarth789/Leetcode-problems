class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def  is_possible(piles,h,m):
            res=0
            for p in piles:
                res+=math.ceil(p/m)
            if res>h:
                return False
            else:
                return True
        s,e=1,max(piles)
        while s<=e:
            m=(s+e)//2
            if is_possible(piles,h,m):
                e=m-1
            else:
                s=m+1
        return s


        