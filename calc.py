print("Welcome to console calcultor")
print("Kindly select the calculation you want to perform from thr following")
option = '''
Addtion --- 1
Subtraction --- 2
Multiplication --- 3
Division --- 4
'''
print(option)
calc = int(input("Enter your selection here: "))

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))


if (calc == 1):
    answer = (a + b)
elif (calc == 2):
    answer = (a - b)
elif(calc == 3):
    answer = (a * b)
elif(calc == 4):
    answer = (a/b)
else:
    print("An unexpexted error has occured, kindly re-select your option")
print("Your answer is ", answer)
    