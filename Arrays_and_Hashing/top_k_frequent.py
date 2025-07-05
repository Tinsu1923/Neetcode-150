class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        res = list()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        while k > 0:
            largest = 0
            element = int()
            for key, value in hashmap:
                if value > largest:
                    largest = value
                    element = key
            res.append(key)
            hashmap.popitem(element)
        return res
                


