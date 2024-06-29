class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = [nums[i : i + 3] for i in range(0, len(nums), 3)]
        for sample in res:
            if sample[-1] - sample[0] > k:
                return []
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 3, 4, 8, 7, 9, 3, 5, 1],
        2,
        [[1, 1, 3], [3, 4, 5], [7, 8, 9]],
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: list[list[int]] = a.divideArray(test[0], test[1])
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
