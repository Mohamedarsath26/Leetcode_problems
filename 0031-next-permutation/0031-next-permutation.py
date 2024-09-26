import itertools
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums to its next lexicographical permutation.
        """
        # Step 1: Generate all unique permutations and sort them
        arr = sorted(set(itertools.permutations(nums)))
        
        # Step 2: Find the current permutation's index
        for i in range(len(arr)):
            if arr[i] == tuple(nums):
                # Step 3: Check if it's not the last permutation
                if i != len(arr) - 1:
                    # Update nums in place to the next permutation
                    nums[:] = list(arr[i + 1])
                else:
                    # If it's the last permutation, return the first one
                    nums[:] = list(arr[0])
                return