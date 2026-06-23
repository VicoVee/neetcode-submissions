class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myArr = {}

        for num in nums:
            if(myArr.get(num)):
                return True
            else:
                myArr[num] = 1
        return False

        
        