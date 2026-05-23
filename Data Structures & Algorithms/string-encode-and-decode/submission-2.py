class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "Empty01"
        return '_appy_'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=='Empty01':
            return []
        return s.split('_appy_')