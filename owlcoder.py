
#count whether the k is set bit or not
'''n=int(input())
k=int(input())
s=1<<k
print(bin(n))
f=n&s
if f>0:
    print(1)
else:
    print(0)'''
#count number of set bits in a number
'''n=int(input())
d=1
c=0
while d<=n:
    if n&d>0:
        c+=1
    
    d=d<<1
print(c)'''
#make zeros from i to lsb
'''n=int(input())
i=int(input())'''
#unique number-two
'''l=[43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]
buck1=[]
buck2=[]
xor=0
for i in range(len(l)):
    xor=xor^l[i]
s=1
while True:
    d=xor&s
    if d>0:
        break
    s=s<<1
print(d)
for i in l:
    if i & d >0:
        buck1.append(i)
    else:
        buck2.append(i)
xb1=0
xb2=0
for i in buck1:
    xb1=xb1^i
for i in buck2:
    xb2=xb2^i
print(xb1,xb2)'''
#LEETCODE POTD
'''from collections import Counter
l=list(map(int,input().split()))
li=[]
d=Counter(l)
p=[]
for v in d.values():
    p.append(v)
a=max(p)
for i in range(1,a+1):
    li.append([])
for i in l:
    j=0
    while j<a:
       
        if i not in li[j]:
            li[j].append(i)
            break
        j+=1
print(li)'''
#LEETCODE POTD
'''from collections import Counter
l=list(map(int,input().split()))
dic=Counter(l)
for k,v in dic.items():
    if v==1:
        print(k)'''

#python bitwise operations
# Using bitwise operation
'''binary_number = int('110101', 2)
count_ones = bin(binary_number).count('1')
print(count_ones) 
n=int(input())
p=[]
l=[]
for i in range(1,n+1):
    d=bin(i)
    f=d[2:]
    p=list(f)
    for i in p:
        if i =='1':
            l.append(int(i))
print(len(l))
n=int(input())
d=bin(n)
s=d[2:]
l=list(s)
print(l)'''
#owlcoder problem
'''l=[17, 5, 6, 1, 12, 11, 1, 12, 17, 19]
q=int(input())
for i in range(q):
    b,c=map(int,input().split())
    d=l[b]
    for i in range(b+1,c+1):
        d=l[i]&d
    print(d)
#owlcoder program
l=[7,3,7,2,3,5]
p=[]
o=[]
q=int(input())
for j in l:
    for i in range(5):
        d=j & 1<<i
        if d >0:
            p.append(1)
        else:
            p.append(0)
    p.reverse()
    
    o.append(p)
    p=[]
print(o)'''

#Hard 
'''l=list(map(int,input().split()))
c=0
for i in range(32):
    for j in l:
        if (j & 1<<i)>0:
            c+=1
    if c>=3:
        print("True")
        break
        
    else:
        c=0
if c==0:
    print("False")'''






    
        

    
        
    
    


    
        
                                                    

            
            
        
        
        
    
    
        





    










    
