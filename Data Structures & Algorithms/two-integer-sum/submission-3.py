class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through each num, subtract with current value,
        # Then find that subtracted value in the list using a hashset?

        myDict = {}
        for i in range(len(nums)):
            myDict[nums[i]] = i

        # print(myDict)
        
        for i in range(len(nums)):
            subTarget = target - nums[i]
            if(subTarget in myDict and myDict[subTarget] > i):
                return [i, myDict[subTarget]]
        
