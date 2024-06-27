class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n: int = len(arr)
        dp: list[int] = [0] * n
        for i in range(n):
            max_val: int = 0
            for j in range(1, k + 1):
                if i - j + 1 >= 0:
                    max_val = max(max_val, arr[i - j + 1])
                    dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + max_val * j)
        return dp[-1]


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 15, 7, 9, 2, 5, 10],
        3,
        84,
    ]
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: int = a.maxSumAfterPartitioning(test[0], test[1])
    print(
        test,
        'got "',
        res,
        '" =>',
        res == test[-1],
    )
    if not (res == test[-1]):
        warn_list.append(f"there is an error in {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
