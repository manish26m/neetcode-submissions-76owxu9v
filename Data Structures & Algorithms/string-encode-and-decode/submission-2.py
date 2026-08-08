class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=str(len(i))+"#"+i
        return ans

    def decode(self, s: str) -> List[str]:
        strs=s
        res,i=[],0
        while i <len(s):
            j=i
            while strs[j] !="#":
                j+=1
            length=int(strs[i:j])
            res.append(strs[j+1:j+1+length])
            i = j + 1 + length
        return res