class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq1={}
        freq2={}
        for i in s:
            freq1[i]=freq1.get(i,0)+1
        for j in t:
            freq2[j]=freq2.get(j,0)+1
        if freq1==freq2:
            return True
        else :
            return False