import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []

        # Push negative freq for max-heap simulation
        for num, freq in d.items():
            heapq.heappush(heap, (-freq, num))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(s.topKFrequent([4,4,4,5,5,6,6,6,6], 2))  # Output: [6, 4]

