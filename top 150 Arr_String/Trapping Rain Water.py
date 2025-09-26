from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    trapped += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    trapped += right_max - height[r]
                r -= 1
        
        return trapped

# Create an object of Solution
sol = Solution()

# Call the trap() method with a test case
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = sol.trap(height)

# Print the result
print("Water trapped:", result)
