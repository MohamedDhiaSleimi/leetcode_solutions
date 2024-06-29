class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers : tuple[str] = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        convertion : tuple[int]    = ( 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        res : int = 0
        for i in range(len(roman_numbers)):
            while s[:len(roman_numbers[i])] == roman_numbers[i]:
                s = s[len(roman_numbers[i]):]
                res += convertion[i]
                print(roman_numbers[i],s,res)
        return res

Solution = Solution()
print(Solution.romanToInt("MCMXCIV"))