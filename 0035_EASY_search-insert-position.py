class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 3, 5, 6],
        5,
        2,
    ],
    [
        [1, 3, 5, 6],
        2,
        1,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: int = a.searchInsert(test[0], test[1])
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
