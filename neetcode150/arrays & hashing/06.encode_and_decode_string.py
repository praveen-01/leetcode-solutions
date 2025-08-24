class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for word in strs:
            encode_str+=str(len(word))+"#"+word
        return encode_str
    
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        j = 0
        while j<len(s):
            if s[j]=="#":
                length = int(s[idx:j])
                word = s[j+1:j+1+length]
                idx = j+1+length
                j = idx
                res.append(word)
            else:
                j+=1                
        return res
