class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res : int = bin(start^goal).count('1')
        return res
