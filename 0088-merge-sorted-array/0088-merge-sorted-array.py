class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0
        index = 0

        arr1 = nums1[:m]
        arr2 = nums2[:n]

        while left < m and right < n:
            if arr1[left] < arr2[right]:
                nums1[index] = arr1[left]
                left+=1

            else:
                nums1[index] = arr2[right]
                right+=1

            index+=1
        
        while(left < m):
            nums1[index] = arr1[left]
            left+=1
            index+=1
  
        while(right < n):
            nums1[index] = arr2[right]
            right+=1
            index+=1