#count whether the k is set bit or not
n=int(input())
k=int(input())
s=1<<k
print(bin(n))
f=n&s
if f>0:
    print(1)
else:
    print(0)
