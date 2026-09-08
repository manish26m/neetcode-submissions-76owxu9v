class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_highest=[0]*n
        right_highest=[0]*n
        l=0
        r=height[n-1]
        i,j=0,n-1
        while i!=n:
            left_highest[i]=l
            right_highest[j]=r
            if height[i]>l:
                l=height[i]
            i+=1
            if height[j]>r:
                r=height[j]
            j-=1
    
        ans=0
        for i in range(n):
            r=min(left_highest[i],right_highest[i])-height[i]
            if r>0:
                ans+=r
        return ans