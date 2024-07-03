class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        else:
            nums.sort()
            return min(nums[len(nums) - 4 + i] - nums[i] for i in range(4))


a: Solution = Solution()
test_cases: list[list] = [
    [
        [5, 3, 2, 4],
        0,
    ],
    [
        [6, 6, 0, 1, 1, 4, 6],
        2,
    ],
    [
        [82, 81, 95, 75, 20],
        1,
    ],
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: int = a.minDifference(test[0])
    if not testing(res, test[-1]):
        warn_list.append(f"{test}->{res}")
    else:
        print("_________________________________\n")
        print(
            test[:-1],
            res,
        )

print("=================================\n")
if warn_list:
    print("errors!!")
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
