passcode="23di1I5ss511I"
total=0
for i in passcode:
    if i.isdigit():
        total=total+int(i)
print(total)