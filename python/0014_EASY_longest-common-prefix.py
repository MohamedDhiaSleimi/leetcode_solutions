class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def prefix(k: int, pre: str) -> bool:
            return all(
                strs[j][k] == pre if i < len(strs[j]) else False
                for j in range(1, len(strs))
            )

        i: int = 0
        res: str = ""
        while i < len(strs[0]) and prefix(i, strs[0][i]):
            res += strs[0][i]
            i += 1
        return res


a: Solution = Solution()
test_cases: list[list] = [
    [
        ["flower", "flow", "flight"],
        "fl",
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: str = a.longestCommonPrefix(test[0])
    print(
        test,
        'got "',
        res,
        '" =>',
        res == test[-1],
    )
    if not (res == test[-1]):
        warn_list.append(f"there is an error in {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
