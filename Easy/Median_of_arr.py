import numpy as np
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge arrays
        merged = np.concatenate((nums1, nums2))
        merged.sort()

        n = len(merged)
        mid = n // 2

        if n % 2 == 1:  # odd length
            return float(merged[mid])
        else:           # even length
            return (merged[mid] + merged[mid - 1]) / 2.0

sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))       # 2.0
print(sol.findMedianSortedArrays([1,2], [3,4]))     # 2.5
