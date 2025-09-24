from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 1. Sort the input array. This is key to the two-pointer approach.
        nums.sort()

        # 2. Iterate through the array to pick the first element 'a'.
        for i, a in enumerate(nums):
            # 3. Skip positive integers. If the first element is > 0,
            # the sum of three numbers cannot be 0.
            if a > 0:
                break
                
            # 4. Skip duplicate values for 'a' to avoid duplicate triplets.
            if i > 0 and a == nums[i - 1]:
                continue

            # 5. Use two pointers for the rest of the array.
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = a + nums[left] + nums[right]

                if current_sum > 0:
                    # Sum is too big, need a smaller number.
                    right -= 1
                elif current_sum < 0:
                    # Sum is too small, need a bigger number.
                    left += 1
                else:
                    # Found a triplet!
                    res.append([a, nums[left], nums[right]])
                    # Move pointers and skip duplicates for 'b' and 'c'.
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        return res

# Example usage:
solver = Solution()
result = solver.threeSum([-1, 0, 1, 2, -1, -4])
print(result) # Output: [[-1, -1, 2], [-1, 0, 1]]