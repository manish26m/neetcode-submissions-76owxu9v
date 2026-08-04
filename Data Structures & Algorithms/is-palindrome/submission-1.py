class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[i.lower() for i in s if i.isalnum()]
        n=len(s)
        i=0
        j=n-1
        if n==0:
            return True
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True