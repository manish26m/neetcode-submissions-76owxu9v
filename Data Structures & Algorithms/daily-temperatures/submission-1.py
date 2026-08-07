class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[]
        ans=[0]*len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            while l and temperatures[i]>=temperatures[l[-1]]:
                l.pop()
            if l:
                ans[i]=l[-1]-i
            l.append(i)
        return ans
