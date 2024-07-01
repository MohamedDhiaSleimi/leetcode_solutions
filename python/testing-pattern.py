a: Solution = Solution()
test_cases: list[list] = []
warn_list: list[str] = []

def testing(res,test) ->bool:
    if isinstance(test, (tuple, list, dict, str, int, float)):
        return res == test
    else:
        raise Exception("did not implement testing function for this class")

for test in test_cases:
    res: bool = a.<methode-name>(test[0])
    if not testing(res,test[-1]):
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
