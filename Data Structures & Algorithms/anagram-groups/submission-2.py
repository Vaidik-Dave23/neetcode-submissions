class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for word in strs:
            sort="".join(sorted(word))
            if sort in freq:
                freq[sort].append(word)
            else:
                freq[sort]=[word]
        result=[]
        for keys,words in freq.items():
            result.append(words)
        return result