'''problem : search a 2d matrix '''
#CODE:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for i in matrix:
            for j in i:
                array.append(j)
        print(array)
        if target in array:
            return True
        else:
            return False
        
