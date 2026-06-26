class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord("a")] += 1
            dict_anagram[tuple(count)].append(word)

        return dict_anagram.values()
            
