class Solution:
    def encode(self, strs: List[str]) -> str:
        output = "" 
        for st in strs: 
            output += str(len(st)) + '#' + st
        return output

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        # take our first ptr i which we know will be an int
        # take a second ptr which is our delimter

        while i < len(s): 
            j = i
            while s[j] != "#": 
                j += 1
            count = int(s[i:j])

            res.append(s[j + 1 : j + count + 1])
            i = j + count + 1
        return res







