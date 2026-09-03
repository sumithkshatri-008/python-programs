class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastzerofound=0
        for current in range(len(nums)):
            if nums[current]!=0:
                nums[lastzerofound],nums[current]=nums[current],nums[lastzerofound]
                lastzerofound+=1
        