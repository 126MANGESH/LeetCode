class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = float('-inf')
        
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            max_area = max(max_area,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r -=1
        return max_area
heights = [1,8,6,2,5,4,8,3,7]
solution = Solution()
result = solution.maxArea(heights)
print("Maximum area:", result)