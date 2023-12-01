pin="3421"
is_digit=pin.isdigit()
is_4digit=(len(pin)==4)
is_valid=is_digit and is_4digit
print(is_valid)