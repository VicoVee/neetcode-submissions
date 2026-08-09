class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Should we sort? time consuming and not o(n)
        # At most nlogn

        # When finding a sequence, we first find the FIRST value in the sequence to start
        # We can use a hashmap to jot down all the values and mark the ones that are the start of the sequence
        # Since the hashmap is o(1) lookup, it should not impact the time complexit

        myMap = {}

        # First add all values in the hashmap, takes only o(n) if not nesting

        for num in nums:
            # set default to 0 for now, which means NOT start of sequence
            myMap[num] = 0

        # For each item in the nums list, see which one is a sequence starter and then store the max

        maxCounter = 0

        # Find when it is the start of the sequence, then proceed to loop
        for num in nums:
            if myMap.get(num-1) == None:
                myMap[num] = 1
           
        for num in nums:
            counter = 0 

            if(myMap.get(num) == 1):
                i = 0
                while (num + i) in myMap:
                    counter += 1
                    i += 1

            if(maxCounter < counter):
                maxCounter = counter
            counter = 0


        return maxCounter


        
