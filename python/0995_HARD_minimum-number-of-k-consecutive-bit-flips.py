class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        flipped: list = [False] * len(nums)
        flipWindows: int = 0
        res: int = 0
        for i in range(len(nums)):
            if i >= k:
                if flipped[i - k]:
                    flipWindows -= 1
            if flipWindows % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                flipWindows += 1
                flipped[i] = True
                res += 1
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        [0, 1, 0],
        1,
        2,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: int = a.minKBitFlips(test[0], test[1])
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
