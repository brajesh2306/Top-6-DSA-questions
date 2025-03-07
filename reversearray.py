a = list(map(int,input().split()))
b = []
for i in range(len(a),0,-1):
    b.append(a[i-1])
print(b)    