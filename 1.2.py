LEN = 3
def circ(y):
    for i in range(y):
        print(f"{' '*(LEN*2)}\x1b[48;5;6m{' '*(LEN*3)}\x1b[0m{' '*LEN*2}",end='')
    print()
    for i in range(y):
        print(f"{' '*LEN}\x1b[48;5;6m{' '*(LEN*5)}\x1b[0m{' '*LEN}",end='')
    print()
    for i in range(y):
            print(f"\x1b[48;5;6m{' '*(LEN*7)}\x1b[0m",end='')
    print()
    for i in range(y):
            print(f"\x1b[48;5;6m{' '*(LEN*7)}\x1b[0m",end='')
    print()
    for i in range(y):
            print(f"\x1b[48;5;6m{' '*(LEN*7)}\x1b[0m",end='')
    print()
    for i in range(y):
        print(f"{' '*LEN}\x1b[48;5;6m{' '*(LEN*5)}\x1b[0m{' '*LEN}",end='')
    print()
    for i in range(y):
        print(f"{' '*(LEN*2)}\x1b[48;5;6m{' '*(LEN*3)}\x1b[0m{' '*LEN*2}",end='')
    print()
a = int(input())
b = int(input())
for i in range(a):        
    circ(b)