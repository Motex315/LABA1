LEN = 3
def x2(y):
    
    for i in range(y):
        if i != y-1:
            if i == 0:
                print(f"^{' '*(LEN*(y-i-2)*2)}\x1b[48;5;6m{' '*(LEN*2)}\x1b[0m")
            else:
                print(f"|{' '*(LEN*(y-i-2)*2)}\x1b[48;5;6m{' '*(LEN*2)}\x1b[0m")

        if i == y-1:
            for i in range(y):
                if i != y-1:
                    print(('-'*3)*2,end='')
                else:
                    print('-'*5+'>',end='')
            print()
x2(15)