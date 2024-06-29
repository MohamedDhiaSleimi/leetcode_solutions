class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write_index: int = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index


a: Solution = Solution()
test_cases: list[list] = [
    [
        [1, 1, 2],
        2,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: bool = a.removeDuplicates(test[0])
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
