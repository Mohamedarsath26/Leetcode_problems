class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for i in range(len(nums)):
            if nums[i]>0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        
        for i in range(len(p)):
            nums[i*2] = p[i]
        for i in range(len(n)):
            nums[(i*2)+1] = n[i]
        return nums
