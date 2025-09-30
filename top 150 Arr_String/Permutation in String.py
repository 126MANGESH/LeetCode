from collections import Counter
import unittest

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:n])
        
        if s1_count == window_count:
            return True
        
        for i in range(n, m):
            window_count[s2[i]] += 1          # add new char
            window_count[s2[i - n]] -= 1      # remove old char
            
            if window_count[s2[i - n]] == 0:  # cleanup
                del window_count[s2[i - n]]
            
            if window_count == s1_count:
                return True
        
        return False


# ✅ Unit Test Cases
class TestCheckInclusion(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.checkInclusion("abc", "lecabee"))  # "cab"

    def test_example2(self):
        self.assertFalse(self.sol.checkInclusion("abc", "lecaabee"))

    def test_same_string(self):
        self.assertTrue(self.sol.checkInclusion("ab", "ab"))

    def test_permutation_at_end(self):
        self.assertTrue(self.sol.checkInclusion("abc", "bbbca"))  # "bca"

    def test_no_match(self):
        self.assertFalse(self.sol.checkInclusion("xyz", "abcdef"))

    def test_single_char_true(self):
        self.assertTrue(self.sol.checkInclusion("a", "cba"))

    def test_single_char_false(self):
        self.assertFalse(self.sol.checkInclusion("z", "cba"))

    def test_large_input(self):
        s1 = "abcd"
        s2 = "efgh" * 250 + "dcba"  # large string, contains permutation
        self.assertTrue(self.sol.checkInclusion(s1, s2))


if __name__ == "__main__":
    unittest.main()