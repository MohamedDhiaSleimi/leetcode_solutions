class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        initial_satisfied: int = sum(
            customers[i] for i in range(len(customers)) if grumpy[i] == 0
        )

        max_additional_satisfied: int = 0
        additional_satisfied: int = 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(
                max_additional_satisfied, additional_satisfied
            )

        return initial_satisfied + max_additional_satisfied


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 0, 1, 2, 1, 1, 7, 5],
        [0, 1, 0, 1, 0, 1, 0, 1],
        3,
        16,
    ],
    [
        [1],
        [0],
        1,
        1,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: bool = a.maxSatisfied(test[0], test[1], test[2])
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
