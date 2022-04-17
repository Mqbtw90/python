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
print(todo_list)


