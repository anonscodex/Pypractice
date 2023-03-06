import random
out = "The number pyhton generated is {}"
x = random.randint(1, 10)
if (x > 5):
    print("Baddest python")
else:
    print("Stupid python")
print(out.format(x))