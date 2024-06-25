class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math as mt

        max: int = int(mt.sqrt(c) + 1)
        for i in range(max):
            if mt.floor(mt.sqrt(c - i**2)) == mt.sqrt(c - i**2):
                return True
        return False
