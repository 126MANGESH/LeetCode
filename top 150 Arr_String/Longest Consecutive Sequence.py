class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)  # for O(1) lookups
        longest = 0
        
        for num in num_set:
            # only check for sequence start
            if num - 1 not in num_set:
                current = num
                streak = 1
                
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                longest = max(longest, streak)
        
        return longest
nums = [100, 4, 200, 1, 3, 2]
sol = Solution()
print(sol.longestConsecutive(nums))  # Output: 4 (sequence: 1,2,3,4)

                



         