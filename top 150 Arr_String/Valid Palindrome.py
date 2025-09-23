from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ""
        for char in s:
            if char.isalnum():
                filtered_s += char.lower()
        if filtered_s == filtered_s[::-1]:
            return True
        else:
            return False