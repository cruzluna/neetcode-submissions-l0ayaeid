class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for ltr in s:
            if ltr not in s_map:
                s_map[ltr] = 1
                continue
            s_map[ltr] = (s_map.get(ltr)+ 1)

        for ltr in t:
            if ltr not in t_map:
                t_map[ltr] = 1
                continue
            t_map[ltr] = (t_map.get(ltr)+ 1)

        return s_map == t_map
        