class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalDict=dict()
        for i in strs:
            freq=[0]*26
            for c in i:
                freq[ord(c) - ord("a")] += 1
            freq=tuple(freq) # If you need to use an array as a key, use it as a tuple!
            finalDict.setdefault(freq, []).append(i)
        finalList=[]
        for key in finalDict:
            finalList.append(finalDict[key])
        return finalList
        

            