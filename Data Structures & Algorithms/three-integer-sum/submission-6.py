class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted? nlogn operation
        # recc n^2 anyway
        # given two pointer

        # -1 0 1 2 3 4 
        # i + j + k = 0
        # i = -j - k
        # if sorted, start at 0 
        # j = i + 1
        # k = len - 1 
        # also check when the current i next value == (remove dups)

        # i = 0 
        res = []

        nums.sort() 

        for i in range(len(nums)-1):
            if(i != 0 and nums[i-1] == nums[i]):
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]


            while (j < k):
                numSum = nums[j] + nums[k]
                if(target == numSum ):
                    res.append([nums[i], nums[j], nums[k]])
                    # Some sort of while loop here
                    j += 1
                    while (j < k and nums[j-1] == nums[j]):
                        j+= 1
                elif(target < numSum):
                    k -= 1
                elif(target > numSum):
                    j += 1

        return res



        

 