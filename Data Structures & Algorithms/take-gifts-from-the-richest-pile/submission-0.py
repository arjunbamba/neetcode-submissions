class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        gifts = [-num for num in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            currMax = -heapq.heappop(gifts)
            currMax = math.floor(math.sqrt(currMax))
            heapq.heappush(gifts, -currMax)
        
        gifts = [-num for num in gifts]
        return sum(gifts)