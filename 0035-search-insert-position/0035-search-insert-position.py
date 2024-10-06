
To solve this problem with an 
\U0001d442
(
log
⁡
\U0001d45b
)
O(logn) runtime complexity, you should use binary search. Since the input array is sorted, binary search will allow you to find the target or the correct insertion index efficiently.

Here’s the solution using binary search:

python
Copy code
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the target is not found, `left` will be the correct insertion index
        return left