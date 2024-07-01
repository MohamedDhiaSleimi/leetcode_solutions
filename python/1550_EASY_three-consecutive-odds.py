class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        consecutive: int = 0
        for i in arr:
            if i % 2 == 0:
                consecutive = 0
            else:
                consecutive += 1
            if consecutive == 3:
                return True
