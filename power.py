#power of a large numbers
a=int(input())
b=int(input())
ans=1

while b:
    if b % 2 !=0:
        b=b-1
        ans=ans*a

    else:
        b=b//2
        a=a*a
print(ans)
        

        
        
