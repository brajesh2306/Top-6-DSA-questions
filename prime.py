a = int(input())
def prime(n):
    if n <2 :
        return False
    for i in range(2, int(n**5)+1):
        if n%i == 0 :
            return False
        return True
b = prime(a)  
if b == True:
    print("prime") 
else:
    print("Not prime")     
        