class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # n = len(nums)
        # ans = set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 ls = [nums[i],nums[j],nums[k]]
        #                 ls.sort()
        #                 ans.add(tuple(ls))

        # res = [list(item) for item in ans]
        # return res


## Better approach
        # n = len(nums)
        # ans = set()
        # for i in range(n):
        #     ls = []
        #     for j in range(i+1,n):
        #         k = -(nums[i] + nums[j])
        #         if k in ls:
        #             temp = [nums[i],nums[j],k]
        #             temp.sort()
        #             ans.add(tuple(temp))
        #         ls.append(nums[j])

        # res = [list(item) for item in ans]

        # return res
        res = []
        n = len(nums)
        nums.sort()
        for i in range(0,n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = n-1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                
                if sum_ < 0:
                    j+=1
                elif sum_ > 0:
                    k-=1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while ( j<k and nums[j] == nums[j-1]):
                        j+=1
                    while (j<k and nums[k] == nums[k+1]):
                        k-=1
                    
        return res
       

