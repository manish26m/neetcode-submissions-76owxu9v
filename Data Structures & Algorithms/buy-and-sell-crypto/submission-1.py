class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #l= buy r=sell
        cheapmax=0
        
        while r<len(prices):
            if prices[l]<prices[r]:
                v=prices[r]-prices[l]
                cheapmax=max(cheapmax,v)
                
            else:
                l=r
            r+=1
        return cheapmax
