number=10
k=1
for i in range(1,number):
    pattern=''
    for j in range(1,i):
        pattern=pattern+str(k)
        k=k+1
    print(pattern)