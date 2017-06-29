#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for index in xrange(len(nums)):
            tmp = target - nums[index]
            if tmp in nums and index != nums.index(tmp):
                result.append(index)
                result.append(nums.index(tmp))
                return result
    #other's solution
    def twoSumiOther(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

if __name__ == "__main__":
    obj = Solution()

    tt = obj.twoSum([3,2,4],6)
    print tt

