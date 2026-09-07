class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashmap = {}

        for i, num in enumerate(nums):
            difference = target - num

            if myHashmap.get(difference) != None:
                return [myHashmap[difference], i]
            else:
                myHashmap[num] = i
        