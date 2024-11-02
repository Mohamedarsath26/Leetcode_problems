class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0, len(nums) - 1
        n = len(nums)
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
    
            if nums[mid] >= target:
                ans =  mid
                high = mid - 1 
            else:
                low = mid + 1
        
        return ans