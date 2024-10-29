class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # left = 0
        # right = 0
        # index = 0

        arr1 = nums1[:m]
        print(arr1)
        arr2 = nums2[:n]
        print(arr2)

        # while left < m and right < n:
        #     if arr1[left] < arr2[right]:
        #         nums1[index] = arr1[left]
        #         left+=1

        #     else:
        #         nums1[index] = arr2[right]
        #         right+=1

        #     index+=1
        
        # while(left < m):
        #     nums1[index] = arr1[left]
        #     left+=1
        #     index+=1
  
        # while(right < n):
        #     nums1[index] = arr2[right]
        #     right+=1
        #     index+=1

        left = m - 1
        right = 0

        # Swap the elements until arr1[left] is smaller than arr2[right]:
        while left >= 0 and right < n:
            if arr1[left] > arr2[right]:
                arr1[left], arr2[right] = arr2[right], arr1[left]
                left -= 1
                right += 1
            else:
                break

        # Sort arr1[] and arr2[] individually:
        arr1.sort()
        arr2.sort()

        nums1[:] = arr1 + arr2

