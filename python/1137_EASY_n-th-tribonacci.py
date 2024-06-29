class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1 :
            return n
        res : list[int] = [1,1,0]
        for _ in range(2,n):
            res.insert(0,sum(res))
            res.pop()
        return res[0]
Solution = Solution()
for i in range(7):
    print(i,":",Solution.tribonacci(i))