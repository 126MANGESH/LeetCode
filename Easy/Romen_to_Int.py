class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        total = 0
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                total -= dic[s[i]]
            else:
                total += dic[s[i]]
        total += dic[s[-1]]  # add the last numeral
        return total
sol = Solution()
print(sol.romanToInt("III"))      # 3
print(sol.romanToInt("LVIII"))    # 58
print(sol.romanToInt("MCMXCIV"))  # 1994
