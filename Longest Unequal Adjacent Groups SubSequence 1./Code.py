class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans=[]
        gp=-1
        for word,group in zip(words,groups):
            if group != gp:
                gp=group
                ans.append(word)
        return ans
