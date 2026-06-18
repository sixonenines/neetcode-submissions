class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif=0
        varb=prices[0]
        for i in range(len(prices)):
            if varb>prices[i]:
                varb=prices[i]
            if prices[i]-varb>dif:
                dif=prices[i]-varb
        return dif