n=5
m=3
for row in range(n):
    each_row=''
    number_in_row=n-row
    for number in range(1,number_in_row):
        each_row=each_row+str(number)+''
    print(each_row)
        