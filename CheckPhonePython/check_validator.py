def valphone(number):
    if len(number) == 10:
        return number[0] == "0" and number[1] == "7" and number.isdigit()
    else:
        return False
phoneInput ='078899198'

print(valphone(phoneInput))
