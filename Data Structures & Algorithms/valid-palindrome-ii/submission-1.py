class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(new_s: str) -> bool: 
            l, r  = 0, len(new_s) - 1
            while l < r: 
                if not new_s[l] == new_s[r]: 
                    return False
                l += 1
                r -= 1
    
            return True

        l, r  = 0, len(s) - 1
        while l < r: 
            if not s[l] == s[r]: 
                return isPalindrome(s[l + 1: r + 1])  or  isPalindrome(s[l:r]) 
            l += 1
            r -= 1

        return True
        