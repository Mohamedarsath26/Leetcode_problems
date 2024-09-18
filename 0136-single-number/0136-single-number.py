class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ##optimal approach
        xor = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            xor = xor^nums[i]
        return xor

        