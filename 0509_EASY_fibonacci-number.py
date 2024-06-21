class Solution:
    def fib(self, n: int) -> int:
        res : list[int] = [0,1]
        for _ in range(n):
            x : int = res[0]
            res[0] = sum(res)
            res[1] = x
        return res[0]

Solution = Solution()
for i in range(12):
    print(Solution.fib(i))