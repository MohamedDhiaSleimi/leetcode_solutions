class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 3 :
            if nums[0] > nums[1] :
                nums = [nums[1],nums[0]]
            else:
                nums = [nums[0],nums[1]]
        else : 
            nums = [self.sortColors([nums[(len(nums)//2):]]),self.sortColors([nums[:(len(nums)//2)]])]
        