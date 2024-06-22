class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res: int = 0
        odd_list: list = [i for i in range(len(nums)) if nums[i] % 2 == 1]
        for i in range(len(odd_list) - k + 1):
            start: int = odd_list[i]
            end: int = odd_list[i + k - 1]
            start_count: int = start - (odd_list[i - 1] if i > 0 else -1)
            end_count: int = (
                odd_list[i + k] if i + k < len(odd_list) else len(nums)
            ) - end
            res += start_count * end_count
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 1, 2, 1, 1],
        3,
        2,
    ],
    [
        [2, 4, 6],
        1,
        0,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: int = a.numberOfSubarrays(test[0], test[1])
    print(
        test,
        "got",
        res,
        "=>",
        res == test[-1],
    )
    if not (res == test[-1]):
        warn_list.append(f"there is an error in {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
