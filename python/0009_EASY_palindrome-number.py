class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x: str = str(x)
        return str_x == str_x[::-1]
