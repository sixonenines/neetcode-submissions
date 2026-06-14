class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairing = [(p,s) for p,s in zip(position,speed)]
        print(pairing)
        pairing.sort(reverse=True)
        fleets=1
        prevTime = (target - pairing[0][0]) / pairing [0][1]
        for i in range(1,len(pairing)):
            currentCar= pairing[i]
            currTime=(target - currentCar[0]) / currentCar [1]
            if currTime > prevTime:
                fleets+=1
                prevTime = currTime
        return fleets