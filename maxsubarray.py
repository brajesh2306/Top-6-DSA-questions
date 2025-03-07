def maxsubarray(n):
    max_sum = float('-inf')
    current_sum = 0 
    for num in n:
        current_sum +=num
        max_sum = max(max_sum,current_sum)
        if current_sum < 0 :
            current_sum = 0
    return max_sum
a = list(map(int,input().split()))  
b = maxsubarray(a)      
print(b)