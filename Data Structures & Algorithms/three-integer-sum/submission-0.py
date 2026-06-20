class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutionArray=[]
        nums.sort()
        for i, startNum in enumerate(nums):
            if startNum>0:
                break
            if i>0 and startNum ==nums[i-1]:
                continue
            # Two pointer
            l,r= i+1, len(nums)-1
            while l<r:
                threeSum=startNum+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    solutionArray.append([startNum,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1]and l<r:
                        l+=1
        return solutionArray