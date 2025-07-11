class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == " " or (not s[l].isalnum()):
                l += 1
                continue
            if s[r] == " " or (not s[l].isalnum()):
                r -= 1
                continue
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                else: 
                    l += 1
                    r -= 1
        return True
    
    
    
    def isPalindrome2(self, s:str) -> bool:
        word = ""
        for i in range(len(s)):
            if s[i].isalnum():
                word += s[i].lower()
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
            
