sum = 2
for i in range(3,100):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        sum+=i
print(sum)        
        
