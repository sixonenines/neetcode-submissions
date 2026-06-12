class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        baseList=[0]*len(temperatures)
        for i in range(len(temperatures)):
            q=i+1
            while q!=len(temperatures): 
                if temperatures[i] < temperatures[q]:
                    baseList[i]=q-i
                    break
                q+=1
        return baseList