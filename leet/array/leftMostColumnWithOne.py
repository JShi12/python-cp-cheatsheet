class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        y,x = binaryMatrix.dimensions()
        foundOne = False
        
        r = x-1
        for y1 in range(y):
            while r >= 0 and binaryMatrix.get(y1, r) == 1:
                r -= 1
                foundOne = True
            if r == -1:
                return 0
        
        if foundOne == False:
            return -1
        else:
            return r+1


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        y,x = binaryMatrix.dimensions()
        
        cury=0
        curx=x-1
        
        while cury < y and curx >= 0:
            if binaryMatrix.get(cury, curx):
                curx -= 1
            else:
                cury += 1
        
        if curx == x-1:
            return -1
        else:
            return curx + 1