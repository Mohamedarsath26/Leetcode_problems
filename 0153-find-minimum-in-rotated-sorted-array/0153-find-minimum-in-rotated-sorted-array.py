class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        high = n-1
        ans = float('inf')
        while(low<=high):

            if nums[low]<nums[high]:
                ans = min(ans,nums[low])
                break

            mid = (low+high)//2

            ans = min(ans,nums[mid])

            if nums[low]<=nums[mid]: ## left half sorted
                ans = min(ans,nums[low])
                low = mid + 1
            else:
                ans = min(ans,nums[mid])
                high = mid - 1

        return ans
        