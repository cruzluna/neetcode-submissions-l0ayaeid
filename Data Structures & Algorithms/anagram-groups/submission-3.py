class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_val_map = defaultdict(list) # {[alphabet 0,1] : [strs]}

        for i, s in enumerate(strs):
            k = [0] * 26
            for letter in s: 
                k[ord(letter) - ord('a')] += 1

            anagram_val_map[tuple(k)].append(strs[i])
            
        return [ x for x in anagram_val_map.values()]

            

        