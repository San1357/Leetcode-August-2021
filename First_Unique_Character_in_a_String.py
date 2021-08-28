'''Problem : First Unique Character in a String '''
#Code :

class Solution:
    def firstUniqChar(self, s: str) -> int:
        array = []
        for i in s:
            if s.count(i)<2 and s.count(i)>0:
                array.append(i)
                return s.index(array[0])
        else:
            return -1
          
