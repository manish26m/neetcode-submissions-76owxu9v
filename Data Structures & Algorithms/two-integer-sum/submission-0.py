class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j= nums
        h={}
        l=len(j)
        for i in range(l):
            a=target-j[i]
            if a in h:
                return [h[a],i] 
            h[j[i]]=i