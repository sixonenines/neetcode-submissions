class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)
        while l<r:
            index=l+((r-l)//2)
            if nums[index]<target:
                l=index+1
            elif nums[index]>=target:
                r=index
        if l<len(nums) and nums[l]==target:
            return l
        else:
            return -1