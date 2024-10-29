from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        arr1 = nums1[:m]  
        arr2 = nums2[:n]  

        i, j = 0, 0
        k = 0  
        

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                nums1[k] = arr1[i]
                i += 1
            else:
                nums1[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            nums1[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            nums1[k] = arr2[j]
            j += 1
            k += 1
