for n in range(2,42):
    if n>0:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
         print(n)