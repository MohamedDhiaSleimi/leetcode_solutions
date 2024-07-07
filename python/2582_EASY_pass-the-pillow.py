class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cond = time // (n - 1)
        if cond % 2 == 0:
            return time % (n - 1) + 1
        else:
            return n - time % (n - 1)


a: Solution = Solution()
test_cases: list[list] = [
    [
        4,
        5,
        2,
    ],
    [
        3,
        2,
        3,
    ],
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: int = a.passThePillow(test[0], test[1])
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
