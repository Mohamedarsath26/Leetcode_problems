class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        n = n1 + n2
        ind2 = n//2
        ind1 = ind2 - 1
        ind1ele = -1
        ind2ele = -1

        i = 0
        j = 0
        cnt = 0
        while(i<n1 and j<n2):
            if nums1[i] < nums2[j]:
                if cnt == ind1:
                    ind1ele = nums1[i]
                if cnt == ind2:
                    ind2ele = nums1[i]
                i+=1
                cnt+=1
            else:
                if cnt == ind1:
                    ind1ele = nums2[j]
                if cnt == ind2:
                    ind2ele = nums2[j]
                j+=1
                cnt+=1
        
        while(i<n1):
            if cnt == ind1:
                ind1ele = nums1[i]
            if cnt == ind2:
                ind2ele = nums1[i]
            i+=1
            cnt+=1

        while(j<n2):
            if cnt == ind1:
                ind1ele = nums2[j]
            if cnt == ind2:
                ind2ele = nums2[j]
            j+=1
            cnt+=1

        if n%2 == 1:
            return ind2ele
        
        else:
            return (ind1ele + ind2ele)/2





            