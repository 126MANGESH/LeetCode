from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Left product
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # Right product
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


# ✅ How to call the function
nums = [1, 2, 3, 4]
solution = Solution()                  # create an object of the class
output = solution.productExceptSelf(nums)  # call the function
print(output)
