from collections import deque

def krotation(arr,k,direction = "left"):
    d = deque(arr)
    if direction == "left":
        d.rotate(-k)
    else:
        d.rotate(k)
    return list(d) 
arr = list(map(int,input().split()))
k = int(input())
direction = input() 
b=krotation(arr,k,direction)      
print(b)