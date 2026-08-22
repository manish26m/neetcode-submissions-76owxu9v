class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=[]
        for i in matrix:
            l.extend(i)
        n=len(l)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if l[mid]==target:
                return True
            elif l[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
