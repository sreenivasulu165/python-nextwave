string="TheLionKing"
length=len(string)
result_string=string[0]
for each_number in range(1,length):
    each_chater=string[each_number]
    upper_case=each_chater.upper()
    lower_case=each_chater.lower()
    if each_chater==upper_case:
        result_string=result_string+"-"+lower_case
    else:
        result_string=result_string + each_chater
print(result_string)