a: Solution = Solution()
test_cases: list[list] = []
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: bool = a.<methode-name>(test[0])
    print(
        test,
        "got \"",
        res,
        "\" =>",
        res == test[-1],
    )
    if not (res == test[-1]):
        warn_list.append(f"there is an error in {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")
