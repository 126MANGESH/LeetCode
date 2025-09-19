from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "$" + s
        return ans    

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            # find the "$"
            while s[j] != "$":
                j += 1
            length = int(s[i:j])  # get the length of the word
            word = s[j+1 : j+1+length]  # extract the word
            ans.append(word)
            i = j + 1 + length  # move pointer to next part
        return ans


sol = Solution()
data = ["leet", "code", "rocks"]
encoded = sol.encode(data)
print("Encoded:", encoded)
decoded = sol.decode(encoded)
print("Decoded:", decoded)

