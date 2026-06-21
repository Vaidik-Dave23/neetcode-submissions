import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        heap=[]
        for key,fre in freq.items():
            heapq.heappush(heap,(fre,key))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result