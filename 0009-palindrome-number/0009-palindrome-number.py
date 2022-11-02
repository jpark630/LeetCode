class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        if list(reversed(s)) == s:
            return True
        else:
            return False
