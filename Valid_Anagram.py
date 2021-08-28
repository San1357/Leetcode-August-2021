'''Problem: Valid Anagram '''
#Code :
#Note sure that it is best solution I think there might be solution which is better than this. i'll see it later soon!!

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array = []
        if  len(s) != len(t):
            return False
        else:
            for i in s:
                if i not in array:
                    array.append(i)
                if i not in t or s.count(i) != t.count(i):
                    return False
                    break
            else:
                return True
