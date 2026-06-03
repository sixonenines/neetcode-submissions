class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num]=1+count.get(num,0)
        # min heap datatructure != heap that I am used to in stack vs heap
        # heapq is basically a binary tree here the smallest element is the root
        # heappush(listHeap, (int, someValue))
        # Interestingly, if there is already an it with that number in the heap, it compares
        # the second element of the tuple. => can crash if not comparable
        # heappop() remove and get smallest element
        heap = []
        for key in count.keys():
            heapq.heappush(heap,(count[key],key))
            # Since we want the to retrieve only the k-frequents elements, we pop
            # the smallest element if the size of the heap is bigger than k
            if len(heap)> k:
                heapq.heappop(heap)
        result=[]
        # One solution, but I prefer list comprehension
        #for i in range(k):
        #    result.append(heapq.heappop(heap)[1])
        #return result
        return [num for _, num in heap]
       