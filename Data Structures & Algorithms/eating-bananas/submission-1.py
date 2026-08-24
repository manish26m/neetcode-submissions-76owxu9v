class Solution:

    def minEatingSpeed(self, piles: List[int], hr: int) -> int:
        maxle=max(piles)
        l=1
        h=maxle
        while l<=h:
            s=0
            mid=(l+h)//2
            for b in piles:
                s+=(b+mid-1)//mid
            if s<=hr:
                h=mid-1
            else:
                l=mid+1
        return l