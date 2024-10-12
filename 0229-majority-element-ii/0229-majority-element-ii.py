class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # hash = {}
        # ls = []
        # for num in nums:
        #     if num in hash:
        #         hash[num] += 1
        #     else:
        #         hash[num] = 1
        # print(hash)
        # max_val = (len(nums)//3)
        # print(max_val)
        
        # for key,val in hash.items():
        #     if val > max_val:
        #         ls.append(key)

        # return ls

        cnt_1 = 0
        cnt_2 = 0
        ele_1 = None
        ele_2 = None
        ls = []
        n_times = (len(nums)//3)
        for i in range(len(nums)):
            if cnt_1 == 0 and ele_2 != nums[i]:
                ele_1 = nums[i]
                cnt_1 = 1
            elif cnt_2 == 0 and ele_1 != nums[i]:
                ele_2 = nums[i]
                cnt_2 = 1
            elif ele_1 == nums[i]:
                cnt_1+=1
            elif ele_2 == nums[i]:
                cnt_2+=1
            else:
                cnt_1-=1
                cnt_2-=1

        cnt_1 = 0
        cnt_2 = 0
        for i in range(len(nums)):
            if nums[i] == ele_1:
                cnt_1+=1
            if nums[i] == ele_2:
                cnt_2+=1

        if cnt_1 > n_times:
            ls.append(ele_1)
        if cnt_2 > n_times:
            ls.append(ele_2)

        return ls




                