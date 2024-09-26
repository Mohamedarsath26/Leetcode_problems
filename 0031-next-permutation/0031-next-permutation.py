from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        This function rearranges numbers into the next lexicographical permutation.
        """
        ind = -1
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the end
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        
        # Step 2: If no such element exists, reverse the entire array
        if ind == -1:
            nums[:] = sorted(nums)
        else:
            # Step 3: Find the element just larger than nums[ind] and swap them
            for i in range(n - 1, ind, -1):
                if nums[i] > nums[ind]:
                    nums[i], nums[ind] = nums[ind], nums[i]
                    break
            
            # Step 4: Reverse the part of the array after the swap index (ind+1 to end)
            nums[ind + 1:] = sorted(nums[ind + 1:])
