'''Problem : TwoSum '''

#CODE : 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        for i in range(nums_length-1):
            for j in range(1, nums_length):
                if i == j:
                    continue
                if nums[i]+ nums[j] == target:
                    return[i,j]
                 
