'''Problem: Intersection Of Two Arrays '''
'''Time : o(n)'''

#CODE :

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sort_nums1 = sorted(nums1)
        sort_nums2 = sorted(nums2)
        i,j = 0,0
        
        result = []
        while i < len(sort_nums1) and j < len(sort_nums2):
            if sort_nums1[i] < sort_nums2[j]:
                i+=1
            elif sort_nums2[j] < sort_nums1[i]:
                j+=1
            else:
                result.append(sort_nums1[i])
                i+=1
                j+=1
        return result
    
