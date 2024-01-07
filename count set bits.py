def fun(n):
    cnt = 0
    i = 0
    while 2 ** i <= n:
        cnt+=1
        i+=1
    return cnt - 1
        
            
        
        

def main_fun(n):
    if n==0:
        return 0
    v=fun(n)
    c=(v*((2**v)//2)+1)+n-(2**v)+main_fun(n-(2**v))
    return c
    


   
n=int(input())
print(main_fun(n))
    
