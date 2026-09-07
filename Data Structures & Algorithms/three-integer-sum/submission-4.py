class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2-Pointer 
        """ num[i] + num[k] + num[j] = 0 
            num[i] = -(num[k] + num[j])

            use two pointers to find j and k
        """
       
       # To avoid duplications, we sort it
       # since for each combination, we dont want the same number in the first position

       # A + B + C = 0 


        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # Check if the value has already been used in A 
            if(i > 0 and a == nums[i-1]):
                continue
            else:
                j = i+1             # Left
                k = len(nums) - 1   # Right

                while( j < k):
                    tmp = a + nums[j] + nums[k]

                    if( tmp > 0 ):
                        k -= 1
                    elif( tmp < 0):
                        j += 1
                    else:
                        res.append( [ a, nums[j], nums[k] ])
                        j += 1
                        # Remember we can still get dups within this loop
                        while( nums[j] == nums[j - 1] and j < k):
                            j += 1

           
        return res

