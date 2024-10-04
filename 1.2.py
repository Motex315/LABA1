def kryg(g):  
    l = 3
    for i in range(g):
        print(f'{' '*(l*2)}\x1b[48;5;6m{' '*(l*3)}\x1b[0m{' '*l*2}',end='')
    print()
    for i in range(g):
        print(f'{' '*l}\x1b[48;5;6m{' '*(l*5)}\x1b[0m{' '*l}',end='')
    print()
    for i in range(g):
            print(f'\x1b[48;5;6m{' '*(l*7)}\x1b[0m',end='')
    print()
    for i in range(g):
            print(f'\x1b[48;5;6m{' '*(l*7)}\x1b[0m',end='')
    print()
    for i in range(g):
            print(f'\x1b[48;5;6m{' '*(l*7)}\x1b[0m',end='')
    print()
    for i in range(g):
        print(f'{' '*l}\x1b[48;5;6m{' '*(l*5)}\x1b[0m{' '*l}',end='')
    print()
    for i in range(g):
        print(f'{' '*(l*2)}\x1b[48;5;6m{' '*(l*3)}\x1b[0m{' '*l*2}',end='')
    print()
a = int(input())
b = int(input())
for i in range(a):        
    kryg(b)