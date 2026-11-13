class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lh=[0]*n
        rh=[0]*n
        l=0
        r=height[n-1]
        i,j=0,n-1
        while i!=n:
            lh[i]=l
            if height[i]>l:
                l=height[i]
            i+=1
            rh[j]=r
            if height[j]>r:
                r=height[j]
            j-=1
        ans=0
        for i in range(n):
            r=min(lh[i],rh[i])-height[i]
            if r>0:
                ans+=r
        return ans