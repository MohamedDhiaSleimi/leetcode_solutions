class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) > 1:
            for i in range(len(s), 0, -1):  
                for j in range(len(s) - i + 1):
                    temp : str = s[j:j+i]
                    if temp == temp[::-1]:
                        return temp
        elif len(s) == 1:
            return s[0]
        else:
            return ""


solution = Solution()
print(solution.longestPalindrome("cbbd"))
