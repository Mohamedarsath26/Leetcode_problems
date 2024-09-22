class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        print(hash)
        max_val = max(hash.values())
        for key,val in hash.items():
            if val == max_val:
                return key