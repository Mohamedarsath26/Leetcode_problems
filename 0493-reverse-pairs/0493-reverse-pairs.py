class Solution:
    def merge(self,nums,low,mid,high):
        temp = []
        left = low
        right = mid+1

        while (left <= mid and right <= high):
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1

        while ( left <= mid):
            temp.append(nums[left])
            left+=1
        while (right <= high):
            temp.append(nums[right])
            right+=1

        for i in range(low,high+1):
            nums[i] = temp[i-low]

    def pair_count(self,nums,low,mid,high):
        cnt = 0
        right = mid+1
        for i in range(low,mid+1):
            while ( right <= high and nums[i] > 2*nums[right]):
                right += 1
            cnt += (right - (mid+1))
        return cnt

        

    def merge_sort(self,nums,low,high):
        cnt = 0
        if low>=high:
            return cnt
        mid = (low+high)//2
        cnt += self.merge_sort(nums,low,mid)
        cnt += self.merge_sort(nums,mid+1,high)
        cnt += self.pair_count(nums,low,mid,high)
        self.merge(nums,low,mid,high)
        return cnt


    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        return self.merge_sort(nums,0,n-1)