class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mis = 0
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                mis = i
        return mis
                