class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        for k in range(len(nums)):
            i=k+1
            j=len(nums)-1
            
            while i<j:
                sums=nums[i]+nums[j]
                target=-(nums[k])
                if target==sums:
                    ll=[nums[k],nums[i],nums[j]]
                    i+=1
                    j-=1
                    if ll in l:
                        continue
                    l.append(ll)
                    
                elif sums>target:
                    j-=1
                else:
                    i+=1
        return l
            

