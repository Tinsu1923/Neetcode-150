class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) 
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> list[str]:
        arr = []
        i = 0
        while i < len(s):
            integer = ""
            word = ""
            while s[i] != '#':
                integer += s[i]
                i += 1
            integer = int(integer)
            i += 1
            for j in range(i, i + integer):
                word += s[j]
            arr.append(word)
            i += integer
                
        return arr