class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a1 = []
        a2 = []
        for i in range(len(nums)):
            if nums[i]!=0:
                a1.append(nums[i])
            else:
                a2.append(nums[i])

        nums[:] = a1+a2