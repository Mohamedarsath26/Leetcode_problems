class Solution:
    def binary_search(self,nums,low,high,target):
            
            while (low<=high):
                mid = (low+high)//2
                if (nums[mid] == target):
                    return mid
                ## check for left sorted
                if nums[low] <= nums[mid]:
                    if nums[low] <= target and target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1   
                else:
                    if nums[mid] <= target and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1

            return -1
            
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.binary_search(nums,0,n-1,target)
            