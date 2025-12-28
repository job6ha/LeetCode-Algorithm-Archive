from typing import List

class Solution:
    def _check_condition_1(self, target, num, num_dict):
        return target - num in num_dict

    def _check_condition_2(self, target, num, idx, num_dict):
        return idx != num_dict[target - num]

    def _check_condition(self, target, num, idx, num_dict):
        return \
            self._check_condition_1(target, num, num_dict) \
            and \
            self._check_condition_2(target, num, idx, num_dict)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {nums[idx]: idx for idx in range(len(nums))}
        for i in range(len(nums)):
            if self._check_condition(target, nums[i], i, num_dict):
                return [i, num_dict[target - nums[i]]]