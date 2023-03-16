import time

name = str(input("Enter your name: "))
time.sleep(1)
greet = ("Welcome " + name)
store = ["apple", "orange", "rice", "beans", "laptop", "phone", "gurasa", "sweet"]
print(greet)
time.sleep(1)
print("select your operation")
option = '''
1 ----- add to store
2 ----- remove from store
'''
print(option)
select = int(input("Enter here: "))
if (select == 1):
    item = str(input("Enter the new item "))
    store.append(item)
    print(store)
elif (select == 2):
    item = str(input("Enter the finished item "))
    store.remove(item)
    print(store)