from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt_1 = 0
        cnt_2 = 0
        ele_1 = None
        ele_2 = None
        ls = []
        n_times = len(nums) // 3
        
        # First pass: Find two potential candidates
        for num in nums:
            if ele_1 == num:
                cnt_1 += 1
            elif ele_2 == num:
                cnt_2 += 1
            elif cnt_1 == 0:
                ele_1 = num
                cnt_1 = 1
            elif cnt_2 == 0:
                ele_2 = num
                cnt_2 = 1
            else:
                cnt_1 -= 1
                cnt_2 -= 1
        
        # Second pass: Count the occurrences of the two candidates
        cnt_1 = 0
        cnt_2 = 0
        for num in nums:
            if num == ele_1:
                cnt_1 += 1
            elif num == ele_2:
                cnt_2 += 1

        # Check if the candidates appear more than n//3 times
        if cnt_1 > n_times:
            ls.append(ele_1)
        if cnt_2 > n_times:
            ls.append(ele_2)

        return ls
