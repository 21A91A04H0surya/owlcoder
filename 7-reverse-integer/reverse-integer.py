class Solution:
    def reverse(self, x: int) -> int:
        k=[]
        if x>=0 and x%10!=0:
            y=str(x)
            z=y[::-1]
            t=int(z)
            if t<2147483647:
                return t
            else:
                return 0
        elif x>=0 and x%10==0:
            b=str(x)
            g=list(b)
            for i in g:
                if i!=0:
                    k.append(i)
            k.reverse()
            a=''.join(k)
            p=int(a)
            if p<2147483647:
                return p
            else:
                return 0
        else:
            k.append('-')
            y=abs(x)
            f=str(y)
            z=f[::-1]
            for i in z:
                k.append(i)
            b=''.join(k)
            m=int(b)
            if m>-2147483648:
                return m
            else:
                return 0
            

        