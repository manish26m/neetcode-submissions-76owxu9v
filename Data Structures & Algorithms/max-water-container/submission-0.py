class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        i=0
        n=len(heights)
        j=n-1
        while i <j:
            m=max(m,(j-i)*(min(heights[i],heights[j])))
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return m
