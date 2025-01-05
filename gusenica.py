import os

LEN = 3

for j in range(150):
    for i in range(3):
            print(f"{' '*j}\x1b[48;5;2m{' '*(LEN*18)}\x1b[0m")
    os.system("cls")
    for i in range(5):
        if i < 1:
            print(f"{' '*j}\x1b[48;5;2m{' '*(LEN*10)}\x1b[0m",end='')
            print(f"{' '*LEN*4}\x1b[48;5;2m{' '*(LEN*5)}\x1b[0m")
        elif i == 3:
            print(f"{' '*j}{' '*(LEN*8)}\x1b[0m{' '*6}",end = '') 
            print(f"\x1b[48;5;2m{' '*(LEN*4)}\x1b[0m")
        elif i == 4:
            print(f"{' '*j}{' '*(LEN*9)}\x1b[0m{' '*6}",end = '') 
            print(f"\x1b[48;5;2m{' '*(LEN*2)}\x1b[0m")
        else:
            print(f"{' '*j}\x1b[48;5;2m{' '*(LEN*19)}\x1b[0m")
    os.system("cls")

