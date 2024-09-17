class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 1
        arr = []
        if len(nums)>1 and max(nums)!=0:
            for i in range(len(nums)):
                if i<len(nums)-1:
                    if nums[i] == nums[i+1] and nums[i]!=0:
                        count+=1
                        arr.append(count)
                    else:
                        count=1
                        arr.append(count)
        else:
            arr = nums 
        return max(arr)

        