string="indian"
count=0
for characher in string:
    if (characher=="a") or (characher=="e") or (characher=="i") or (characher=="o") or (characher=="u"):
        count=count+1
        s=int(count)
if s>=4:
    print("less than 3")
else:
    print('greter than 3')
    
