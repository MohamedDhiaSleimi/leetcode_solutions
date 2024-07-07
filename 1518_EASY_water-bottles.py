class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res: int = numBottles
        while numBottles >= numExchange:
            res += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        9,
        3,
        13,
    ],
    [
        15,
        4,
        19,
    ],
]
warn_list: list[str] = []


def testing(res, test) -> bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    res: int = a.numWaterBottles(test[0], test[1])
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
