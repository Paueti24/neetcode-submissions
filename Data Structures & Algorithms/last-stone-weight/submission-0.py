class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if (x != y):
                heapq.heappush(heap, y - x)
        
        if len(heap) == 0:
            return 0
        # else -> 1 stone
        return -heap[0]
        