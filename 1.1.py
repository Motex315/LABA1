LEN = 3

for i in range(4):
    print(f"\x1b[48;5;7m{' '*(LEN*5)}",end='')
    print(f"\x1b[48;5;4m{' '*(LEN*3)}",end='')
    print(f"\x1b[48;5;7m{' '*(LEN*10)}\x1b[0m")

for i in range(3):
    print(f"\x1b[48;5;4m{' '*(LEN*18)}\x1b[0m")
    
for i in range(4):
    print(f"\x1b[48;5;7m{' '*(LEN*5)}",end='')
    print(f"\x1b[48;5;4m{' '*(LEN*3)}",end='')
    print(f"\x1b[48;5;7m{' '*(LEN*10)}\x1b[0m")