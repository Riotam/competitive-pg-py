# 五目並べ
import utils

table = utils.get_lines(5)

if table[0][0] != '.' and table[0][0] == table[1][1] and table[0][0] == table[2][2] and table[0][0] == table[3][3] and table[0][0] == table[4][4]:
    print(table[0][0])
    exit()

if table[0][4] != '.' and table[0][4] == table[1][3] and table[0][4] == table[2][2] and table[0][4] == table[3][1] and table[0][0] == table[4][0]:
    print(table[0][0])
    exit()

for row in table:
    if row == 'OOOOO':
        print('O')
        exit()
    elif row == 'XXXXX':
        print('X')
        exit()

for i in range(5):
    if table[0][i] != '.' and table[0][i] == table[1][i] and table[0][i] == table[2][i] and table[0][i] == table[3][i] and table[0][i] == table[4][i]:
        print(table[0][i])
        exit()

print('D')
