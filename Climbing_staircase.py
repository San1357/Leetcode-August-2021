'''Problem : Climbing Staircase '''

#CODE :

class Solution:
    def climbStairs(self, n: int) -> int:
      if n <=2:
        return n
      x = 1
      y = 2
      for i in range(3,n):
        x,y = y, x+y
      return x + y
