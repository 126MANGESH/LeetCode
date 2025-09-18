from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            # Sort each word, use it as a key
            dic["".join(sorted(word))].append(word)

        return list(dic.values())
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
