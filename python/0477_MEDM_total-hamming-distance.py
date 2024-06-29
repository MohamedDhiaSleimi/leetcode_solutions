class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        num_len : int = len(bin(max(nums))[2:])
        occurences_pos : list[list[bool]]= [[0 for _ in range(2)] for _ in range(num_len)]
        for num in nums: 
            for i, element in enumerate(bin(num)[2:].zfill(num_len)):
                occurences_pos[i][int(element)] += 1

        res : int = 0
        for i in range(num_len):
            for num1 in range(2):
                for num2 in range(num1 + 1, 2):
                    res += occurences_pos[i][num1] * occurences_pos[i][num2]
        return res

Solution = Solution()
test_cases : list[list[int]] = [[4,14,2],[4,14,4]]
for i in test_cases :
    print(Solution.totalHammingDistance(i))