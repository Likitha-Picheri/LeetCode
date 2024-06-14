class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        y=[]
        for z in words:
            t=z.rsplit(separator)
            y.extend(t)
        while(1):
            if "" in y:
                y.remove("")
            else:
                break
        return y
        
