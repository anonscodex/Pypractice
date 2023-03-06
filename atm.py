pin = int(input("Input your pin: "))
if (pin == 1234 or pin == 1111 or pin == 0000):
    amount = int(input("amount: "))
    if (amount > 10000):
        print("insufficient balance")
    else:
        print("Take your cash")
        print("Thank you using our atm")
else:
    print("Wrong pin Thief!!!!!!!!!!!!!!")