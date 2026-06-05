class Solution:

    def encode(self, strs: List[str]) -> str:
        # idea: not only encode a seperator sign, but also the length of the word to make
        # decoding easier
        encodedStr=""
        for i in strs:
            length=str(len(i))
            encodedStr+=length+"#"+i
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedArr=[]
        i=0
        while i<len(s):
            j=i
            while s[j] !="#": # Find the delimiter
                j+=1
            # Now you can get the length
            length=int(s[i:j])
            # The string starts after the delimiter and ends after + length 
            decodedArr.append(s[j+1:j+1+length])
            i = j+1+length # set i to position of final char of string
        return decodedArr