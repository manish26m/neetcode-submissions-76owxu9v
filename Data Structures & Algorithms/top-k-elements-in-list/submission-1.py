class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kk={}
        z=[]
        for i in nums:
            kk[i]=kk.get(i,0)+1
        z = sorted(kk, key=kk.get, reverse=True)

        return z[:k]