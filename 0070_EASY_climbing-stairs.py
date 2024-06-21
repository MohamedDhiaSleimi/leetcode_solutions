class Solution:
    def climbStairs(self, n: int) -> int:
        res : list[int] = [1,1]
        for i in range(n):
            x : int = res[0]
            res[0] = sum(res)
            res[1] = x
        return res

Solution = Solution()
for i in range(6):
    print(i,Solution.climbStairs(i))