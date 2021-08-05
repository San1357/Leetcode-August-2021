'''PRoblem : Remove Elements '''

#CODE : 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0
        while i<len(nums):
            print(i)
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
                
