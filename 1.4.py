a = []
with open('sequence.txt') as input:
    a = [float(i) for i in input]

p=0
m=0
for i in range(len(a)):
    if a[i] < 10 and a[i] > 5 :
        p+=1
    if a[i] > -10 and a[i] < -5 :
        m+=1
pr = round(m/(m+p)*100)
print(f'\x1b[48;5;6m{' '*pr}\x1b[48;5;3m{' '*(100-pr)}\x1b[0m')
print('Числа от -10 до -5 -',round((m/(m+p))*100,2),'%',' '*45+'Числа от 5 до 10 -',round((p/(m+p))*100,2),'%')