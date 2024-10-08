class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums[:] = sorted(nums)  Bruteforece solution

        # Better Solution
        # cnt = 0
        # cnt_1 = 0
        # cnt_2 = 0

        # for i in range(len(nums)):
        #     if (nums[i]==0):
        #         cnt+=1
        #     elif (nums[i] == 1):
        #         cnt_1+=1
        #     elif (nums[i]==2):
        #         cnt_2+=1
        # for i in range(cnt): #0 to 2
        #     print(i)
        #     nums[i] = 0
        # for i in range(cnt,cnt+cnt_1): # 2 to 4
        #     print(i)
        #     nums[i] = 1
        # for i in range(cnt+cnt_1,cnt_1+cnt_2+cnt): # 4 to 6
        #     print(i)
        #     nums[i] = 2

        # Optimized solution

        low = 0
        mid = 0
        high = len(nums)-1

        while mid<=high:
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
                
