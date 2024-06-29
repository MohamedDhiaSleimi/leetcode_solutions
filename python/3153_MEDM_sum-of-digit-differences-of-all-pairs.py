class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        num_len = len(str(nums[0]))
        occurences_pos : list[list[int]]= [[0 for _ in range(10)] for _ in range(num_len)]

        for num in nums:
            for i, element in enumerate(str(num)):
                occurences_pos[i][int(element)] += 1
        
        total_diff = 0
        for i in range(num_len):
            for num1 in range(10):
                for num2 in range(num1 + 1, 10):
                    if occurences_pos[i][num1] != 0 and occurences_pos[i][num2] != 0:
                        total_diff += occurences_pos[i][num1] * occurences_pos[i][num2]
        return total_diff

Solution = Solution()
test_cases : list[list[int]] = [[13,23,12],[68,66],[10,10,10,10,10]]
for i in test_cases:
    print(Solution.sumDigitDifferences(i))