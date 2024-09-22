class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = [0]*21

        for i in range(len(nums)):
            hash[nums[i]]+=1
        print(hash)

        val = max(hash)
        return hash.index(val)