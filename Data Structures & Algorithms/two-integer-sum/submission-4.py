class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts={}
        for i in range(len(nums)):
            num=nums[i]
            searchedTarget=target-num
            if searchedTarget in dicts:
                return [dicts[searchedTarget],i]
            dicts[num] = i
        ## ENUMERATE DOES index and value:

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dicts:
                return [dicts[diff], i]
            dicts[n]= i
