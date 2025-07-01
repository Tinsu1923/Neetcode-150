from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        s_hash = {}
        t_hash = {}
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        
        for chars in s_hash:
            if s_hash[chars] != t_hash.get(chars,0): return False
        return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram3(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)