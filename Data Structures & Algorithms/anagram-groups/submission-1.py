class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        l=[]
        hashing={}
        for i in strs:
            f=[0]*26
            for j in i:
                f[ord(j)-ord('a')]+=1
            f=tuple(f)
            if f not in hashing:
                hashing[f]=[]
            
            hashing[f].append(i)
        for i in hashing.values():
            l.append(i)


        return l
            
