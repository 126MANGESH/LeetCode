class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
sol = Solution()
print(sol.lengthOfLongestSubstring("zxyzxyz"))  # 3
print(sol.lengthOfLongestSubstring("xxxx"))     # 1
print(sol.lengthOfLongestSubstring("pwwkew"))   # 3
