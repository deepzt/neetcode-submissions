class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        for el in range(len(nums)):
            if target-nums[el] in nums[el+1:]:
                my_list.append(el)
                my_list.append(nums.index(target-nums[el], el+1))
                break

        return my_list