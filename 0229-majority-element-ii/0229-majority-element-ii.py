class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        ls = []
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        print(hash)
        max_val = (len(nums)//3)
        print(max_val)
        
        for key,val in hash.items():
            if val > max_val:
                ls.append(key)

        return ls
                