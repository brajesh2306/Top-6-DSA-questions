def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**5)+1):
        if n%i ==0:
            return False
        return True
sum = 0    
a = list(map(int,input().split()))
for i in a:
    b = prime(i)
    if b == True:
        sum +=i
print(sum)            