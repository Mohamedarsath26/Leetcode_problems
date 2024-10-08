class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_tree(nums,target,boo):
            low = 0
            high = len(nums) - 1
            idx = -1
            while low<=high:
                mid = (low+high)//2

                if nums[mid] > target:
                    high = mid-1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    idx = mid
                    if boo:
                        high = mid - 1
                    else:
                        low = mid + 1

            return idx

        left = bin_tree(nums,target,True)
        right = bin_tree(nums,target,False)

        return [left,right]
                    

        