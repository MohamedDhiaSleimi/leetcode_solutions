

class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        max_prof_diff: list = [0]*(max(difficulty)+1)
        for d,p in zip(difficulty,profit):
            if max_prof_diff[d] < p:
                max_prof_diff[d] = p
        for i in range(1,len(max_prof_diff)):
            if max_prof_diff[i] < max_prof_diff[i-1]:
                max_prof_diff[i] = max_prof_diff[i-1]
        res: int = 0
        for i in worker:
            if i >= len(max_prof_diff)-1:
                res += max_prof_diff[-1]
            else :
                res += max_prof_diff[i]
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        [2,4,6,8,10],
        [10,20,30,40,50],
        [4,5,6,7],
        100,
    ],
    [
        [85,47,57],
        [24,66,99],
        [40,25,25],
        0,
    ],
    [
        [68,35,52,47,86],
        [67,17,1,81,3],
        [92,10,85,84,82],
        324,
    ],
    [
        [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63],
        [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77],
        [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16],
        1392,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: int = a.maxProfitAssignment(test[0],test[1],test[2])
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
