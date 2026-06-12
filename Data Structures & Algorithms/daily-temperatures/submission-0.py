class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        baseList=[]
        for i in range(len(temperatures)):
            q=i+1
            cond=True
            while q!=len(temperatures): 
                if temperatures[i] < temperatures[q]:
                    cond=False
                    baseList.append(q-i)
                    break
                q+=1
            if cond:
                baseList.append(0)
        return baseList