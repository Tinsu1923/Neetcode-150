from collections import defaultdict
class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())
