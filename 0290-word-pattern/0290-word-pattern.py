class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dict={}
        stringa=s.split()
        if len(pattern)!=len(stringa):
            return False
        if len(set(pattern))!=len(set(stringa)):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]]=stringa[i]
                print( dict[pattern[i]])
            else:
                if dict[pattern[i]]!=stringa[i]:
                    print( dict[pattern[i]],stringa[i])
                   
                    return False
        return True