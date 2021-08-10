'''Problem: sqrt(x) '''

#code:

class Solution:
    def mySqrt(self, x: int) -> int:
      left = 1
      right = 0
      mid = 0
      while(left<mid):
        mid = left + math.floor((right-left)/2)
        if (mid**2 > x):
          right = mid
        elif (mid**2) ==x:
          return mid 
        else:
          left = mid +1
      return left -1
          
          
