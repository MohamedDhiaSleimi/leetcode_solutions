class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:

        def canPlaceBalls(min_dist):
            count: int = 1
            last_position: int = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        position.sort()

        left: int = 1
        right: int = int((position[-1] - position[0]) / (m - 1))
        while left <= right:
            mid: int = int((left + right + 1) // 2)
            if canPlaceBalls(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 2, 3, 4, 7],
        3,
        3,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: bool = a.maxDistance(test[0], test[1])
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
