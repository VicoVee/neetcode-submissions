class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHashmap = {}

        for num in nums:
            if myHashmap.get(num) != None:
                return True
            else:
                myHashmap[num] = 1 
        
        return False
        