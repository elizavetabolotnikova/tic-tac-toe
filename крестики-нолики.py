feild = [['-'] * 3 for i in range(3)]
def instruction():
    print('Добро пожаловать в игру в крестики нолики!')
    print('-----------------------------------------')
    print('Формат ввода:номер строки, затем номер столбца')
    print('после этого на той же строке введите за кого вы играете')
    print('Английская X-крестики, английская O-нолики')
def show_feild():
    print(' ', 0, 1, 2, sep=' | ', end=" | \n")
    for i in range(len(feild)):
        print('---------------')
        print(i, *feild[i], sep=' | ', end=' | \n')
    print('---------------')


def ask():
    cnt=0
    while True:
        cnt += 1
        position = input('Введите клетку и крестик или нолик').split()
        if len(position) == 3:
            if position[0].isdigit() and position[1].isdigit() and (position[2] == 'X' or position[2] == 'O'):
                x, y, X_or_O = position
        else:
            print('Некорректный ввод')
            break
        x = int(x)
        y = int(y)
        if feild[x][y] == '-':
            feild[x][y] = X_or_O
            show_feild()
        if cnt == 9:
            print('Ничья')
            break
        if (feild[2][0] == feild[1][1] == feild[0][2] != '-') or (feild[0][0] == feild[1][1] == feild[2][2] != '-') or (feild[0][0] == feild[0][1] == feild[0][2] != '-') or (
                feild[1][0] == feild[1][1] == feild[1][2] != '-') or (
                feild[2][0] == feild[2][1] == feild[2][2] != '-') or (
                feild[0][0] == feild[1][0] == feild[2][0] != '-') or (
                feild[0][1] == feild[1][1] == feild[2][1] != '-') or (feild[0][2] == feild[1][2] == feild[2][2] != '-'):
            print('Победа',X_or_O,'!!!')
            break
instruction()
show_feild()
ask()


