n=5
start_number=0
for num in range(1,n+1):
    start_number=start_number+num
for row in range(n):
    each_row=''
    left_spaces=""*(2*row)
    for column in range(n-row):
        each_row=each_row+str(start_number)+""
        start_number=start_number-1
        each_row=each_row
    print(each_row)