class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert number to string
        s = str(x)
        # Check if string is equal to its reverse
        return s == s[::-1]


# Example usage
sol = Solution()
print(sol.isPalindrome(121))  # True
print(sol.isPalindrome(-121)) # False
print(sol.isPalindrome(10))   # False
