class Solution:
    # def lower_bound(self,a,n,x):
    #     low = 0
    #     high = n-1
    #     ans = n
    #     while (low<=high):
    #         mid = (low+high)//2
    #         if a[mid] >= x:
    #             ans = mid
    #             high = mid - 1
    #         else:
    #             low = mid +1
    #     return ans

    # def upper_bound(self,a,n,x):
    #     low = 0
    #     high = n-1
    #     ans = n
    #     while (low<=high):
    #         mid = (low+high)//2
    #         if a[mid] > x:
    #             ans = mid
    #             high = mid - 1
    #         else:
    #             low = mid +1
    #     return ans

    def lower_bound(self,a,n,x):
        low = 0
        high = n-1
        ans = n
        while (low<=high):
            mid = (low+high)//2
            if a[mid] == x:
                ans = mid
                high = mid - 1
            elif a[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def upper_bound(self,a,n,x):
        low = 0
        high = n-1
        ans = n
        while (low<=high):
            mid = (low+high)//2
            if a[mid] == x:
                ans = mid
                low = mid + 1
            elif a[mid] < x:
                low = mid +1
            else:
                high = mid - 1
        return ans


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        lb = self.lower_bound(nums,n,target) # gives the first occurence
        print(lb)
        if (lb == n or nums[lb] != target):
            return [-1,-1]
        else:
            ub = self.upper_bound(nums,n,target)  # gives the last occurence

        return [lb,ub]

