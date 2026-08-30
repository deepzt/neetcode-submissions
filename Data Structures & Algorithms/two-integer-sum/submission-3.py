class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,v in enumerate(nums):
            hashmap[v] = i
        #{3:0, 4:1, 5:2, 6:3}
        #target = 7
        for i,v in enumerate(nums): #(0,3), (1,4), (2, 5), (3,6)
            diff = target - v
            if diff in hashmap and hashmap[diff]!=i:
                return [i, hashmap[diff]]
        return 
