class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end=len(numbers)-1
        front=0
        while numbers[front]+numbers[end]!=target and end!=front:
            if numbers[front]+numbers[end]>target:
                end-=1
            if numbers[front]+numbers[end]<target:
                front+=1
        return [front+1,end+1]
        