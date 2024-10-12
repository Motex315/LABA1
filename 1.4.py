NUM = []

with open('sequence.txt') as input:
    a = [float(i) for i in input]

pos=0
neg=0

for i in range(len(a)):
    if a[i] < 10 and a[i] > 5 :
        pos+=1
    if a[i] > -10 and a[i] < -5 :
        neg+=1

percn = round(neg/(neg+pos)*100)
percp = 100 - percn

print(f"\x1b[48;5;6m{' '*percn}\x1b[48;5;3m{' '*percp}\x1b[0m")

print('Числа от -10 до -5 -',round((neg/(neg+pos))*100,2),'%',end='')
print(' '*45+'Числа от 5 до 10 -',round((pos/(neg+pos))*100,2),'%')