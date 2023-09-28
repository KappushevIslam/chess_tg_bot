import telebot


bot = telebot.TeleBot('6559147374:AAFM3ZZ4kSx48uIzCvcVRpndndTecuHoX_s')


class Figure:
    """
    Класс фигуры. в нем хранится вся информация о фигуре:
    какая конкретно это фигура (её может и не быть), её цвет и координаты.
    """
    def __init__(self, row, col, figure='.', color='w'):  # инициализируем каждую фигуру
        self.figure = figure
        self.color = color
        self.row = int(row)
        self.col = int(col)

    def __str__(self):
        return self.figure

    def get_possible_moves(self, board):
        """
        находит координаты всех возможных ходов для нашей фигуры.
        возвращает список, в котором каждый элемент - координаты
        возможного хода формата (строка, колонна)
        функция работает только для желтых, поэтому если на вход
        попалась красная фигура, то мы полностью реверсим доску и
        потом работает с каждой фигурой
        """
        if board[self.row][self.col].color == 'r':  # тот самый реверс
            is_red = True
            board = list(reversed([list(reversed(i)) for i in board]))
            self.row = 7 - self.row
            self.col = 7 - self.col
        else:
            is_red = False
        piece = str(board[self.row][self.col])
        moves = []
        if piece == '.':
            return moves
        if piece == 'P':  # поиск ходов для пешки
            if self.row != 7 and board[self.row+1][self.col].figure == '.':
                moves += [(self.row+1, self.col)]
            if self.row == 1 and board[self.row+2][self.col].figure == '.':
                moves += [(self.row+2, self.col)]
            if self.row + 1 < 8 and self.col + 1 < 8:
                if board[self.row+1][self.col+1].color == 'y' if is_red else board[self.row+1][self.col+1].color == 'r':
                    moves += [(self.row+1, self.col+1)]
            if self.row + 1 < 8 and self.col - 1 > -1:
                if board[self.row+1][self.col-1].color == 'y' if is_red else board[self.row+1][self.col-1].color == 'r':
                    moves += [(self.row+1, self.col-1)]
        if piece == 'N':  # для коня
            if self.row < 6 and self.col < 7 and (board[self.row+2][self.col+1].figure == '.' or (board[self.row+2][self.col+1].color == 'y' if is_red else board[self.row+2][self.col+1].color == 'r')):
                moves += [(self.row+2, self.col+1)]
            if self.row < 7 and self.col < 6 and (board[self.row+1][self.col+2].figure == '.' or (board[self.row+1][self.col+2].color == 'y' if is_red else board[self.row+1][self.col+2].color == 'r')):
                moves += [(self.row+1, self.col+2)]
            if self.row < 6 and self.col > 0 and (board[self.row+2][self.col-1].figure == '.' or (board[self.row+2][self.col-1].color == 'y' if is_red else board[self.row+2][self.col-1].color == 'r')):
                moves += [(self.row+2, self.col-1)]
            if self.row < 7 and self.col > 1 and (board[self.row+1][self.col-2].figure == '.' or (board[self.row+1][self.col-2].color == 'y' if is_red else board[self.row+1][self.col-2].color == 'r')):
                moves += [(self.row+1, self.col-2)]
            if self.row > 1 and self.col < 7 and (board[self.row-2][self.col+1].figure == '.' or (board[self.row-2][self.col+1].color == 'y' if is_red else board[self.row-2][self.col+1].color == 'r')):
                moves += [(self.row-2, self.col+1)]
            if self.row > 0 and self.col < 6 and (board[self.row-1][self.col+2].figure == '.' or (board[self.row-1][self.col+2].color == 'y' if is_red else board[self.row-1][self.col+2].color == 'r')):
                moves += [(self.row-1, self.col+2)]
            if self.row > 1 and self.col > 0 and (board[self.row-2][self.col-1].figure == '.' or (board[self.row-2][self.col-1].color == 'y' if is_red else board[self.row-2][self.col-1].color == 'r')):
                moves += [(self.row-2, self.col-1)]
            if self.row > 0 and self.col > 1 and (board[self.row-1][self.col-2].figure == '.' or (board[self.row-1][self.col-2].color == 'y' if is_red else board[self.row-1][self.col-2].color == 'r')):
                moves += [(self.row-1, self.col-2)]
        if piece == 'B' or piece == 'Q':  # для слона и ходов ферзя, которые как у слона
            right_down_flag = 0
            right_up_flag = 0
            left_down_flag = 0
            left_up_flag = 0
            for i in range(1, 8):
                if self.row + i < 8 and self.col + i < 8 and right_down_flag == 0:
                    if board[self.row+i][self.col+i].figure == '.':
                        moves += [(self.row+i, self.col+i)]
                    elif board[self.row+i][self.col+i].color == 'y' if is_red else board[self.row+i][self.col+i].color == 'r':
                        moves += [(self.row+i, self.col+i)]
                        right_down_flag = 1
                    else:
                        right_down_flag = 1
                if self.row + i < 7 and self.col - i > -1 and left_down_flag == 0:
                    if board[self.row+i][self.col-i].figure == '.':
                        moves += [(self.row+i, self.col-i)]
                    elif board[self.row+i][self.col-i].color == 'y' if is_red else board[self.row+i][self.col-i].color == 'r':
                        moves += [(self.row+i, self.col-i)]
                        left_down_flag = 1
                    else:
                        left_down_flag = 1
                if self.row - i > -1 and self.col + i < 8 and right_up_flag == 0:
                    if board[self.row-i][self.col+i].figure == '.':
                        moves += [(self.row-i, self.col+i)]
                    elif board[self.row-i][self.col+i].color == 'y' if is_red else board[self.row-i][self.col+i].color == 'r':
                        moves += [(self.row-i, self.col+i)]
                        right_up_flag = 1
                if self.row - i > -1 and self.col - i > -1 and left_up_flag == 0:
                    if board[self.row-i][self.col-i].figure == '.':
                        moves += [(self.row-1, self.col-i)]
                    elif board[self.row-i][self.col-i].color == 'y' if is_red else board[self.row-i][self.col-i].color == 'r':
                        moves += [(self.row-i, self.col-i)]
                        left_up_flag = 1
                    else:
                        left_up_flag = 1
        if piece == 'R' or piece == 'Q':  # для ладьи и ходов ферзя, которые как у ладьи
            up_flag = 0
            down_flag = 0
            left_flag = 0
            right_flag = 0
            for i in range(1, 8):
                if self.row + i < 8 and down_flag == 0:
                    if board[self.row + i][self.col].figure == '.':
                        moves += [(self.row + i, self.col)]
                    elif board[self.row + i][self.col].color == 'y' if is_red else board[self.row + i][self.col].color == 'r':
                        moves += [(self.row + i, self.col)]
                        down_flag = 1
                    else:
                        down_flag = 1
                if self.row - i > -1 and up_flag == 0:
                    if board[self.row - i][self.col].figure == '.':
                        moves += [(self.row - i, self.col)]
                    elif board[self.row - i][self.col].color == 'y' if is_red else board[self.row - i][self.col].color == 'r':
                        moves += [(self.row - i, self.col)]
                        up_flag = 1
                    else:
                        up_flag = 1
                if self.col + i < 8 and right_flag == 0:
                    if board[self.row][self.col + i].figure == '.':
                        moves += [(self.row, self.col + i)]
                    elif board[self.row][self.col + i].color == 'y' if is_red else board[self.row][self.col + i].color == 'r':
                        moves += [(self.row, self.col + i)]
                        right_flag = 1
                    else:
                        right_flag = 1
                if self.col - i > -1 and left_flag == 0:
                    if board[self.row][self.col - i].figure == '.':
                        moves += [(self.row, self.col - i)]
                    elif board[self.row][self.col - i].color == 'y' if is_red else board[self.row][self.col - i].color == 'r':
                        moves += [(self.row, self.col - i)]
                        left_flag = 1
                    else:
                        left_flag = 1
        if piece == 'K':  # для короля
            moves_c = 0  # если король походил хоть раз, то рокировка невозможна
            if self.row + 1 < 8 and self.col + 1 < 8 and (board[self.row+1][self.col+1].figure == '.' or
                (board[self.row+1][self.col+1].color == 'y' if is_red else board[self.row+1][self.col+1].color == 'r')):
                moves += [(self.row + 1, self.col + 1)]
            if self.row + 1 < 8 and (board[self.row+1][self.col].figure == '.' or
                (board[self.row+1][self.col].color == 'y' if is_red else board[self.row+1][self.col].color == 'r')):
                moves += [(self.row+1, self.col)]
            if self.row + 1 < 8 and self.col - 1 > -1 and (board[self.row+1][self.col-1].figure == '.' or
                (board[self.row+1][self.col-1].color == 'y' if is_red else board[self.row+1][self.col-1].color == 'r')):
                moves += [(self.row+1, self.col-1)]
            if self.col - 1 > -1 and (board[self.row][self.col-1].figure == '.' or
                (board[self.row][self.col-1].color == 'y' if is_red else board[self.row][self.col-1].color == 'r')):
                moves += [(self.row, self.col-1)]
            if self.row - 1 > -1 and self.col - 1 > -1 and (board[self.row-1][self.col-1].figure == '.' or
                (board[self.row-1][self.col-1].color == 'y' if is_red else board[self.row-1][self.col-1].color == 'r')):
                moves += [(self.row-1, self.col-1)]
            if self.row - 1 > -1 and (board[self.row-1][self.col].figure == '.' or
                (board[self.row-1][self.col].color == 'y' if is_red else board[self.row-1][self.col].color == 'r')):
                moves += [(self.row-1, self.col)]
            if self.row - 1 > -1 and self.col + 1 < 8 and (board[self.row-1][self.col+1].figure == '.' or
                (board[self.row-1][self.col+1].color == 'y' if is_red else board[self.row-1][self.col+1].color == 'r')):
                moves += [(self.row-1, self.col+1)]
            if self.col + 1 < 8 and (board[self.row][self.col+1].figure == '.' or
                (board[self.row][self.col+1].color == 'y' if is_red else board[self.row][self.col+1].color == 'r')):
                moves += [(self.row, self.col+1)]
        if is_red:  # так как сы реверсили доску, то нужно возможные ходы сделать применимыми к обычной доске, а не реверснутой
            moves = list(map(lambda x: (7-x[0], 7-x[1]), moves))
            self.row = 7 - self.row
            self.col = 7 - self.col
        return moves

    def make_move(self, x_to, y_to, board): # функция делает ход, если он возможен
        print(board[self.row][self.col].get_possible_moves(board), (x_to, y_to))
        if (x_to, y_to) in board[self.row][self.col].get_possible_moves(board):
            board[x_to][y_to] = Figure(x_to, y_to, board[self.row][self.col].figure, board[self.row][self.col].color)
            board[self.row][self.col] = Figure(self.row, self.col, '.', 'w')
        else:
            print('Невозможный ход')


class Board:
    board = []  # Сама доска
    rows = 8  # кол-во строк
    columns = 8  # кол-во столбцов
    board_graphics = ''

    def make_board(self):  # формируем игровое поле
        # самое главное - доска. представляет собой двумерный массив
        self.board = [
            [Figure(0, 0, 'R', 'y'), Figure(0, 1, 'N', 'y'), Figure(0, 2, 'B', 'y'), Figure(0, 3, 'Q', 'y'), Figure(0, 4, 'K', 'y'), Figure(0, 5, 'B', 'y'), Figure(0, 6, 'N', 'y'), Figure(0, 7, 'R', 'y')],
            [Figure(1, 0, 'P', 'y'), Figure(1, 1, 'P', 'y'), Figure(1, 2, 'P', 'y'), Figure(1, 3, 'P', 'y'), Figure(1, 4, 'P', 'y'), Figure(1, 5, 'P', 'y'), Figure(1, 6, 'P', 'y'), Figure(1, 7, 'P', 'y')],
            [Figure(2, 0), Figure(2, 1), Figure(2, 2), Figure(2, 3), Figure(2, 4), Figure(2, 5), Figure(2, 6), Figure(2, 7)],
            [Figure(3, 0), Figure(3, 1), Figure(3, 2), Figure(3, 3), Figure(3, 4), Figure(3, 5), Figure(3, 6), Figure(3, 7)],
            [Figure(4, 0), Figure(4, 1), Figure(4, 2), Figure(4, 3), Figure(4, 4), Figure(4, 5), Figure(4, 6), Figure(4, 7)],
            [Figure(5, 0), Figure(5, 1), Figure(5, 2), Figure(5, 3), Figure(5, 4), Figure(5, 5), Figure(5, 6), Figure(5, 7)],
            [Figure(6, 0, 'P', 'r'), Figure(6, 1, 'P', 'r'), Figure(6, 2, 'P', 'r'), Figure(6, 3, 'P', 'r'), Figure(6, 4, 'P', 'r'), Figure(6, 5, 'P', 'r'), Figure(6, 6, 'P', 'r'), Figure(6, 7, 'P', 'r')],
            [Figure(7, 0, 'R', 'r'), Figure(7, 1, 'N', 'r'), Figure(7, 2, 'B', 'r'), Figure(7, 3, 'Q', 'r'), Figure(7, 4, 'K', 'r'), Figure(7, 5, 'B', 'r'), Figure(7, 6, 'N', 'r'), Figure(7, 7, 'R', 'r')],
        ]

    def display_board(self):  # Вывод графической части
        board_graphics = ''
        for i, row in enumerate(self.board):
            row = list(map(lambda x: ' ' + x.color + x.figure + '  ' if x.figure != '.' else f'   {x.figure}   ', row))
            if i + 1 == 10:
                board_graphics += f"{''.join(row)}\n"
                break
            board_graphics += f"{''.join(row)}\n"
        self.board_graphics = board_graphics
        return self.board_graphics


class Game:
    board = Board()
    board.make_board()
    convert_letter = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
    move_counter = 0
    move_from = ''
    move_to = ''
    color_to_move = 'r'


class TextMessage:
    """
    Служебный класс, для флагов и запоминания последнего сообщения.
    была проблема с видимостью простых переменных, поэтому пришлось
    сделать класс. наверно это можно сделать лучше, но и так работает.
    Можно сказать, что это немного костыль, но я не согласен :)
    """
    def __init__(self, text, flag=0, chess_on=0):
        self.text = text
        self.flag = flag
        self.chess_on = chess_on


written_message = TextMessage('Еще ничего нет, ты не писал')
game = Game()


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Записать")
    btn2 = telebot.types.KeyboardButton("Отправить")
    btn3 = telebot.types.KeyboardButton("Играть шахматы")
    markup.add(btn1, btn2, btn3)
    with open('big_floppa.gif', 'rb') as gif:
        bot.send_animation(message.chat.id, gif, caption='Привет, активист ЦТ!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Записать':
        bot.send_message(message.chat.id, 'Введи сообщение, которое хочешь записать')
        written_message.flag = 1
    elif message.text == 'Отправить':
        bot.send_message(message.chat.id, written_message.text)
    elif message.text == 'Играть шахматы':
        bot.send_message(message.chat.id, f'{game.board.display_board()}\n Введите ход, очередь {game.color_to_move}. Для выхода отправьте "q"')
        written_message.chess_on = 1
    elif written_message.flag == 1:
        written_message.text = message.text
        written_message.flag = 0
        bot.send_message(message.chat.id, 'Сообщение записано!')
    elif written_message.chess_on == 1:
        usr_inp = message.text
        if usr_inp == 'q':
            written_message.chess_on = 0
            game.board.make_board()
            game.move_counter = 0
            game.color_to_move = 'r'
        else:
            for i in usr_inp:
                if i in game.convert_letter:
                    usr_inp = usr_inp.replace(i, game.convert_letter[i])
            usr_inp = usr_inp.split('-')
            move_from = (8 - int(usr_inp[0][-1]), int(usr_inp[0][-2]))
            move_to = (8 - int(usr_inp[1][-1]), int(usr_inp[1][-2]))
            possible_move_flag1 = 1
            possible_move_flag2 = 1
            if game.board.board[move_from[0]][move_from[1]].figure == '.':
                bot.send_message(message.chat.id, 'Там не фигуры, шахматист)')
                possible_move_flag1 = 0
            elif game.board.board[move_from[0]][move_from[1]].color != game.color_to_move:
                bot.send_message(message.chat.id, 'Сейчас ход фигуры другого цвета')
                possible_move_flag2 = 0
            if possible_move_flag1 * possible_move_flag2 == 1:
                try:
                    game.board.board[move_from[0]][move_from[1]].make_move(move_to[0], move_to[1], game.board.board)
                    game.move_counter += 1
                    game.color_to_move = 'r' if game.move_counter % 2 == 0 else 'y'
                    bot.send_message(message.chat.id, f'{game.board.display_board()}\n Введите ход, очередь {game.color_to_move}')
                except:  # знаю, что эксепт без указания ошибки - гавнокод, но у меня было мало времени)
                    bot.send_message(message.chat.id, 'Невозможный ход, шахматист, попробуй другой)')
    else:
        bot.send_message(message.chat.id, 'Не понимаю тебя')


bot.polling(none_stop=True)
