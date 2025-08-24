class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in freq_map:
                freq_map[sorted_word].append(word)
            else:
                freq_map[sorted_word] = [word]
        return [val for val in freq_map.values() ]