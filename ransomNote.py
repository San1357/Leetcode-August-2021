'''Problem: ransomNote '''
#Code:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        array = []
        for i in magazine:
            if i not in array:
                array.append(i)
        for i in ransomNote:
            if ransomNote.count(i) <= magazine.count(i):
                if i not in array:
                    return False
            else:
                return False
        else:
            return True
