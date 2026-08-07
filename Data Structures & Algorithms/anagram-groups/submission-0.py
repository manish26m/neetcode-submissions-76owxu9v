class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        k={}
        d=[]
        for i in strs:
            o=[0]*26
            for j in i:
                o[ord(j)-ord('a')]+=1
            key=tuple(o)
            if key not in k:
                k[key]=[]
            k[key].append(i)
        for i in k.values():
            d.append(i)
        return d
