def invitation():
  print('''
   ————————————————————————————————————————————
  | Добро пожаловать в игру "Крестики-нолики"! |
   ————————————————————————————————————————————
  ''')

def rules():
  print('''
  |                   ПРАВИЛА                  |
  |   Два игрока по очереди ставят свой знак   |
  |  (крестик или нолик) на свободные клетки   |
  |  поля.  Первый, выстроивший в ряд 3 своих  |
  |    фигуры по вертикали, горизонтали или    |
  |          диагонали, выигрывает.            |
  |   Формат ввода хода: х(строка) у(столбец)  |
  ''')

def new_game():
  print('''
    ————————————
   | НОВАЯ ИГРА |
    ————————————
  ''')

def draw_field():
    print(f"    | 0 | 1 | 2 |")
    print('  —— ——— ——— ———')
    for i in range(3):
        print(f"  {i} | {' | '.join(field[i])} |")
        print('  —— ——— ——— ———')

def ask():
    while True:
        coordinates = input('Ваш ход:').split()
    
        if len(coordinates) != 2:
            print('Введите две координаты!')
            continue
        
        x, y = coordinates
        
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue
        
        x, y = int(x), int(y)
        
        if not(0 <= x <= 2) or not(0 <= y <= 2):
            print('Неверные координаты!')
            continue
        
        if field[x][y] != ' ':
            print('Клетка занята!')
            continue
        
        return x, y

def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)),  # 0 строка
              ((1, 0), (1, 1), (1, 2)),  # 1 строка
              ((2, 0), (2, 1), (2, 2)),  # 2 строка
              ((0, 0), (1, 0), (2, 0)),  # 0 столбец
              ((0, 1), (1, 1), (2, 1)),  # 1 столбец
              ((0, 2), (1, 2), (2, 2)),  # 2 столбец
              ((0, 0), (1, 1), (2, 2)),  # главная диагональ
              ((0, 2), (1, 1), (2, 0)))  # побочная диагональ
    for coord in win_coord:
        symbols = []
        for pos in coord:
            symbols.append(field[pos[0]][pos[1]])
        if symbols[0] == symbols[1] == symbols[2] != ' ':
            print(f'''
               ——————————————————
              |    Выиграл {symbols[0]}!    |
               ——————————————————
                ''')
            return True
    return False


invitation()
rules()
answer = 'да'
while answer == 'да':
    step = 0
    new_game()
    field = [[" " for j in range(3)] for i in range(3)]
    while True:
        step += 1
        draw_field()
        if step % 2 == 1:
            print('Ходит крестик')
        else:
            print('Ходит нолик')
    
        x, y = ask()
        if step % 2 == 1:
            field[x][y] = 'x'
        else:
            field[x][y] = 'o'
    
        if check_win():
            draw_field()
            break
    
        if step == 9:
            print('''
             ————————
            | Ничья! |
             ————————
              ''')
            break

    answer = input("Сыграть еще раз? да/нет ")
    if answer == "да":
        continue
    else:
        print('''
           ———————
          | ПОКА! |
           ———————
        ''')
        break
