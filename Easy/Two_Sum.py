
class Solution:
    def twoSum(self, nums, target):
        seen = {}  # store number -> index mapping
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


sol = Solution()

print(sol.twoSum([2,7,11,15], 9))  # [0, 1]
print(sol.twoSum([3,2,4], 6))      # [1, 2]
print(sol.twoSum([3,3], 6))        # [0, 1]
