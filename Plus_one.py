'''Problem : PlusOne '''

#CODE :

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        x  = len(digits)-1
        plus_one = 0
        array2 = []
        
        for i in range(x,-1,-1):
            plus_one = digits[i] + carry
            if  plus_one >= 10:
                carry = 1
            else:
                carry = 0
            array2.append(plus_one % 10)
            i-=1
            
        if carry == 1:
            array2.append(1)
            return array2[::-1]
        else:
            return array2[::-1]
        
