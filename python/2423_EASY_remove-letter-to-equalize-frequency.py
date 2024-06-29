class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter

        char_count = Counter(word)

        for char in word:
            char_count[char] -= 1

            if char_count[char] == 0:
                del char_count[char]

            freq_set = set(char_count.values())

            if len(freq_set) == 1:
                return True

            char_count[char] += 1

        return False


a: Solution = Solution()
test_cases: list[list] = [
    ["abcc", True],
    ["aazz", False],
    ["bac", True],
    ["zz", True],
    ["cccd", True],
    ["babbdd", False],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: bool = a.equalFrequency(test[0])
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
