myLab = [['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*'],
         ['*','*', '*','*','*', '*','*','*', '*','*']]
while True:
    b = int(input("vvedite stroku"))
    n = int(input("stolbec"))
    myLab[b][n] = '0'
    for stroka in myLab:
        for symb in stroka:
            print(symb, end="")
        print()
print(myLab)
