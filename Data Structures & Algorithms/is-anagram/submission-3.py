class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use a hashset to count the chars

        sHash = {}
        tHash = {}

        # Check if the length is the same 
        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            if(sHash.get(s[i])):
                sHash[s[i]] += 1
            else:
                sHash[s[i]] = 1

            if(tHash.get(t[i])):
                tHash[t[i]] += 1
            else:
                tHash[t[i]] = 1

        return sHash == tHash
            