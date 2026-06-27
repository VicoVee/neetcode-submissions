class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Following the optimial solution 
        
        # First create a hashmap that will store the character counts : list of words

        myMap = defaultdict(list) # Sets the default value of any added key as an empty List[]

        # Loop through each string
        for word in strs:
            count = [0] * 26 # Create a count list, with 26 values representing the 26 letters of the alphabet

            # store the character count in the count list above using ASCII
            # Use ord(char) to get the ASCII value of the character a = 65
            for char in word:
                count[ord(char) - ord('a')] += 1

            # After getting the count, check if the count has already been stored as a key in the myMap
            # else add it and append the word to the list
            # For python, a list cannot be a key, so it was converted to a tuple

            # myMap { ([1,1,3,4,5, ....]): [cat, tac, ...], (0,0,0...): [mat, tam, ...]}
            myMap[tuple(count)].append(word)

        # Since myMap is a dictionary of the countList : list of words, just get the list of words via
        # the values() 
        # myMap.values => dictValues([....]), use list to convert to a list of values


        return list(myMap.values())