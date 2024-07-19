class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if '-' in n:
            for i in range(1,len(n)):
                print(int(n[i]))
                if int(n[i])>x:
                    print(n[i])
                    return n[:i]+str(x)+n[i:]
            else:
                return n+str(x)

        else:
            for i in range(len(n)):
                if int(n[i])<x:
                    print(n[i])
                    return n[:i]+str(x)+n[i:]
            else:
                return n+str(x)

        # digits=list(map(int,list(n)))
        # print(digits)
        # digits.append(x)
        # digits.sort(reverse=True)
        # return ''.join(str(d) for d in digits)
        