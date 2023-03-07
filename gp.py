score = int(input("Enter your score to get equivalent in letter "))
if (score <= 100 and score >= 90):
    print("You have A")
elif (score <= 89 and score >= 80):
    print("You have B")
elif (score <=79 and score >= 70):
    print("You have C")
elif (score <= 69 and score >= 60):
    print("You have D")
elif (score <= 59 and score >= 50):
    print("You have E")
else:
    print("You have F")