class Solution:
    def distMoney(self, money: int, children: int) -> int:
        res: int = 0
        if money >= children:
            res = money // 8
            if res > children:
                res = children - 1
            if (res * 8) != money and children - res == 0:
                res -= 1
            if children - res == 1 and money - (res * 8) == 4:
                res -= 1
            while children - res > money - (res * 8):
                res -= 1

            return res
        else:
            return -1


a: Solution = Solution()
test_cases: list[list[int]] = [
    [20, 3, 1],
    [16, 2, 2],
    [1, 2, -1],
    [2, 2, 0],
    [17, 2, 1],
    [8, 2, 0],
    [16, 10, 0],
]
for test in test_cases:
    res: int = a.distMoney(test[0], test[1])
    print(
        test,
        "got",
        res,
        "expected",
        test[2],
        test[2] == res,
    )
