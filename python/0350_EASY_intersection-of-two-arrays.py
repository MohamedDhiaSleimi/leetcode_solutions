class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res: list[int] = []
        short, long = sorted([nums1, nums2], key=lambda x: len(x))
        for i in short:
            if i in long:
                res.append(i)
                long.remove(i)
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 2, 2, 1],
        [2, 2],
        [2, 2],
    ],
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: list = a.intersect(test[0], test[1])
    if not testing(res, test[-1]):
        warn_list.append(f"{test},{res}")
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
