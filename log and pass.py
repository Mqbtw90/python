a = "kolos"
b = 2345
c = input("vvedite login")
d = int(input("vvedite parol`"))
while(a != c) or (b != d):
    if(a != c) and (b == d):
        print("neverniy login")
    if(a == c) and (b != d):
        print("neverniy porol`")
    c = input("vvedite login")
    d = int(input("vvedite parol`"))
print("vse verno")
