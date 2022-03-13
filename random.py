import random
a = random.randint(1, 5)
num = int(input("vvedite chislo"))
while(num != a):
    if(num > a):
        print("> a")
    if(num < a):
        print("< a")
    num = int(input("vvedite chislo"))
if(num == a):
    print("vi nashli chislo")
    print("v tochku")
