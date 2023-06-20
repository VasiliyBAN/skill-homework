game_field = list(range(1, 10))


def field_area():
    print('-' * 7 + 'Tic-Tac-Toe' + '-' * 7)
    print('-' * 9 + 'Ver_0.1' + '-' * 9)
    print()
    print('-' * 19)
    for i in range(3):
        print('| ', game_field[0 + i * 3], ' | ', game_field[1 + i * 3], ' | ', game_field[2 + i * 3], ' | ')
        print('-' * 19)


def game_move(player_move):
    while True:
        value = input('Куда запишем ' + player_move + '?\n>>>')
        if not (value in '123456789'):
            print('Ошибка, повторите')
            continue
        value = int(value)
        if str(game_field[value - 1]) in 'XO':
            print('Клетка занята, повторите')
            continue
        game_field[value - 1] = player_move
        break


win_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def check_win():
    for check in win_comb:
        if game_field[check[0] - 1] == game_field[check[1] - 1] == game_field[check[2] - 1]:
            return game_field[check[1] - 1]
    return False


def GAME():
    move = 0
    while True:
        field_area()
        if move % 2 == 0:
            game_move('X')
        else:
            game_move('O')

        if move > 1:
            win = check_win()
            if win:
                field_area()
                print('Выиграли ' + win)
                break
        move += 1
        if move > 8:
            field_area()
            print('Ничья!')
            break


GAME()
