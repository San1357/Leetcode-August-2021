'''Problem : Search Insert Position '''

#code :

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(0,len(nums)):
            if nums[i] >= target:
                return i 
            else:
                i+=1
        return n
                
