todo_list=[]
while True:
    command=input("vvedite komandu")
    if command == "d":
        a= input("kakoe delo dobavit`?")
        todo_list.append(a)
    elif command == "r":
        for prod in todo_list:
            print(prod)
    elif command == "u":
        c=input("chto hochesh ubrat`")
        todo_list.remove(c)
    elif command =="p":
        n = int(input("chto hochesh perepisat`?"))
        m = input("na chto chto hochesh imenit`" )
        todo_list[n] = m
    elif command =="v":
        y = int(input("chto vivesti"))
        l = y-1
        print(todo_list[l])
