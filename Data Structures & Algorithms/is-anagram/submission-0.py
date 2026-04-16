class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h={}
        for i in s:
            h[i]=h.get(i,0)+1
        for i in t:
            h[i]=h.get(i,0)-1
            if h[i]==0:
                del h[i]
        return len(h)==0

