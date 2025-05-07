class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        for i in range(int(len(str(x))/2), len(str(x))):
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                return False
        
        return True
