class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Bucket sort
        # Idea: Since max freq==len(nums), create a list of length len(nums)
        # where index 1 => all nums that appeared 1x total and so on..

        # Get better at list comprehensions
        freq=[[] for i in range(len(nums)+1)] # +1 since max freq==len(nums)
        count={}

        for num in nums:
            count[num]=count.get(num,0)+1
        for key,value in count.items():
            freq[value].append(key)
        
        result=[]
        for i in range(len(freq)-1,0,-1): # Work in reverse
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result