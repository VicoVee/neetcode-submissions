class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        # Check if the length is the same 
        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            sHash[s[i]] = sHash.get(s[i], 0) + 1
            tHash[t[i]] = tHash.get(t[i], 0) + 1

        return sHash == tHash