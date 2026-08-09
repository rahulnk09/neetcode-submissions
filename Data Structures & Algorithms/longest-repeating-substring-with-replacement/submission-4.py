class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        l=0
        res=0

        for r in range(len(s)):
            freq[ord(s[r])-ord('A')]+=1
            maxfreq=max(freq)

            if (r-l+1)-maxfreq<=k:
                res=max(res,(r-l+1))

            else:
                while (r-l+1)-maxfreq>k:
                    freq[ord(s[l])-ord('A')]-=1
                    maxfreq=max(freq)
                    l+=1
        return res