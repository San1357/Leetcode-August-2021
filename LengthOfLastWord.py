'''Problem : Length Of LAst Word '''

#CODE :

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        print("lst", lst)
        if len(lst) == 0:
            return 0
        else:
            return len(lst[-1])
        
