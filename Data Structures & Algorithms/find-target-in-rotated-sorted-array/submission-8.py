class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[l]<nums[m]:
                if nums[l]<=target<nums[m]:
                    """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1