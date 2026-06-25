class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol=0
        l, r=0, len(heights)-1
        while l < r:
            smallerBar=heights[r] # min()
            if heights[l]<heights[r]:
                smallerBar=heights[l]
            width=r-l
            tempVol=width*smallerBar
            if tempVol>maxVol:
                maxVol=tempVol
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxVol
