#Котуранова Мария Сергеевна 408879
# ЛАБОРАТОРНАЯ РАБОТА №1
print("1 ЗАДАНИЕ")
RED= '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK= '\u001b[40m'
END = '\u001b[0m'
print(f'{WHITE}{" "*5}{BLUE}{" " * 3}{BLUE}{" " * 3}{WHITE}{" "*15}{END}')
print(f'{WHITE}{" "*5}{BLUE}{" " * 3}{BLUE}{" " * 3}{WHITE}{" "*15}{END}')
print(f'{BLUE}{" " * 24}  {END}')
print(f'{BLUE}{" " * 24}  {END}')
print(f'{WHITE}{" "*5}{BLUE}{" " * 3}{BLUE}{" " * 3}{WHITE}{" "*15}{END}')
print(f'{WHITE}{" "*5}{BLUE}{" " * 3}{BLUE}{" " * 3}{WHITE}{" "*15}{END}')

print("2 ЗАДАНИЕ")
print("Введите длину узора")
n=int(input())
print('Ведите ширину узора')
b=int(input())

for i in range(b):
    print(f'{WHITE}{" "*3}{BLACK}{" " *6}{WHITE}{" "*6}{BLACK}{" " * 6}{WHITE}{" "*3}{END}'*n, sep='')
    print(f'{WHITE}{" "*1}{BLACK}{" " * 10}{WHITE}{" " * 2}{BLACK}{" " * 10}{WHITE}{" " * 1}{END}'*n, sep='')
    print(f'{BLACK}{" " * 12}{BLACK}{" " * 12}{END}'*n, sep='')
    print(f'{WHITE}{" "*1}{BLACK}{" " * 10}{WHITE}{" " * 2}{BLACK}{" " * 10}{WHITE}{" " * 1}{END}'*n, sep='')
    print(f'{WHITE}{" " * 3}{BLACK}{" " * 6}{WHITE}{" " * 6}{BLACK}{" " * 6}{WHITE}{" " * 3}{END}'*n, sep='')




print('3 ЗАДАНИЕ')
plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 0.5

step = 1
print(result)

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 0.5


for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

print("ЗАДАНИЕ 4")
f=open("seqyence.txt")
cnt1=0
cnt2=0
for i in f:
    s = float(i)
    if (5<s<10) or (-10<s<-5):
        cnt1+=1
    cnt2+=1
per = round((cnt1/cnt2)*100)
print(per)
print(f'{RED}{" "*per}{BLUE}{" "*(100-per)}{END}')
