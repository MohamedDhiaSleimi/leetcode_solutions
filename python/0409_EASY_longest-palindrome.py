class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_repeats : str = ""
        result : int = 0
        for i in s:
            if i in s_repeats :
                continue
            else :
                repeats : int = s.count(i) // 2
                if repeats > 0 :
                    result += repeats * 2
                s_repeats += i
        if result == len(s):
            return result
        else :
            return result + 1


solution = Solution()
print(solution.longestPalindrome("tattarrattat"))
