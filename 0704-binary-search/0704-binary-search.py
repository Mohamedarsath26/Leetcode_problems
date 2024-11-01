from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid  # Return the index of the target
            elif nums[mid] < target:
                low = mid + 1  # Move the low pointer to the right of mid
            else:
                high = mid - 1  # Move the high pointer to the left of mid

        return -1  # Return -1 if the target is not found
