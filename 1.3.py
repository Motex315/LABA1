def x2(y):
    l = 3
    for i in range(0,y):
        if i != y-1:
            if i == 0:
                print(f'^{' '*(l*(y-i-2)*2)}\x1b[48;5;6m{' '*(l*2)}\x1b[0m')
            else:
                print(f'|{' '*(l*(y-i-2)*2)}\x1b[48;5;6m{' '*(l*2)}\x1b[0m')

        if i == y-1:
            for i in range(y):
                if i != y-1:
                    print(('-'*3)*2,end='')
                else:
                    print('-'*5+'>',end='')
            print()
x2(15)