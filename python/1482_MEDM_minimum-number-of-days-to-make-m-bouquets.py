class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(days: int) -> bool:
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False
        
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        return low









a: Solution = Solution()
test_cases: list = [
    [
        [1,10,3,10,2],
        3,
        1,
        3,
    ],
    [
        [1,10,3,10,2],
        3,
        2,
        -1,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: bool = a.minDays(test[0],test[1],test[2])
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
