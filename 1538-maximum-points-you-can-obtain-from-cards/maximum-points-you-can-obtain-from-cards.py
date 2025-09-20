class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        left=sum(cardPoints[:k])
        right=0
        m=left
        for i in range(k):
            left=left-cardPoints[k-i-1]
            right=right+cardPoints[n-i-1]
            m=max(m,right+left)
        return m
