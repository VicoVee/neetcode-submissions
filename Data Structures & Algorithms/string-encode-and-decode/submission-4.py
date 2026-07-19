class Solution:

    def encode(self, strs: List[str]) -> str:
        # Hack, for python create a string using an array, then merge at the end
        result = []

        # To do the encoding, we must find a way to separate each word
        # Natively, we can use a delimiter. However, the requirements states that the 
        # string can contain ANY ASCII character. As a result, using delimiters like , can mess it up
        
        # Rather than a single delimiter, you can combine it with the length of the string, so 
        # you can pull the right amount of characters even if it has the delimiter in it
        for string in strs:
            result.append(str(len(string)))
            result.append('#')
            result.append(string)

        results = "".join(result)
        # print(results)
        return results

    def decode(self, s: str) -> List[str]:
        # With our number and # delimter, loop each character of the string and append the word
        # to a list

        result = []
        start = 0 
        index = 0
        while(index < len(s)):
            if(s[index] == '#'):
                length = int(s[start:index])
                word = s[index + 1: index + 1 + length]
                result.append(word)
                start = index + 1 + length
                index = start
            else:
                index += 1 
        return result

