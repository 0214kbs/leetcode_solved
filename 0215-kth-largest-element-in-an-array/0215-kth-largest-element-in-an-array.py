import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for n in nums:
            heapq.heappush(hq, -n)

        for _ in range(k-1):
            heapq.heappop(hq)
        val = heapq.heappop(hq)
        return -val