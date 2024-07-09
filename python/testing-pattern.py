a = Solution()
test_cases = []
warn_list = []


def testing(res, expected) -> bool:
    if isinstance(expected, (tuple, list, dict, str, int, float)):
        return res == expected
    else:
        raise Exception("did not implement testing function for this class")


for test in test_cases:
    input_value = test[0]
    expected_result = test[-1]

    try:
        res = a.sample_method(input_value)
    except Exception as e:
        warn_list.append(f"{test},{str(e)}")
        continue

    if not testing(res, expected_result):
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
else:
    print("All tests passed!")
