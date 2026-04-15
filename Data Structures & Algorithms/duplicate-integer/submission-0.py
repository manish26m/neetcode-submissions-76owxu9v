class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash=MyHash(len(nums))
        for i in nums:
            if hash.search(i)==True:
                return True
            hash.insert(i)
            
            
        return False
        
class MyHash:
    def __init__(self,n):
        self.b=n
        self.table=[[] for x in range(n)]
    def insert(self,x):
        i=x%self.b
        self.table[i].append(x)
    def remove(self,x):
        i=x%self.b
        if x in self.table[i]:
            self.table[i].remove(x)
    
    def search(self,x):
        i=x%self.b
        return x in self.table[i]
