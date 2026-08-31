class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []

        for el in strs:
            sorted_s = tuple(sorted(el))
            hashmap[sorted_s].append(el)
        for value in hashmap.values():
            result.append(value)
            
        return(result)