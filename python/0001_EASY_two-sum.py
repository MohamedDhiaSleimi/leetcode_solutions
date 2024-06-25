class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res : list[int] = []
        for i in nums :
            for j in nums[nums.index(i)+1:] :
                if i+j == target :
                    res.append(nums.index(i))
                    res.append(len(nums)-1-nums[::-1].index(j))
                    return res

Solution = Solution()
print(Solution.twoSum([3,3],6))
