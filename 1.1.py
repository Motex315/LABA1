l = 3
for i in range(4):
    print(f'\x1b[48;5;7m{' '*(l*5)}\x1b[48;5;4m{' '*(l*3)}\x1b[48;5;7m{' '*(l*10)}\x1b[0m')
for i in range(3):
    print(f'\x1b[48;5;4m{' '*(l*18)}\x1b[0m')
for i in range(4):
    print(f'\x1b[48;5;7m{' '*(l*5)}\x1b[48;5;4m{' '*(l*3)}\x1b[48;5;7m{' '*(l*10)}\x1b[0m')