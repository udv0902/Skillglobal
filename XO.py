board = list(range(1, 10))  # создаем список полей


# функция для прорисовки игрового поля
def draw_board():
	print('-------------')
	for i in range(3):
		print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
	print('-------------')


# выбор и правильность ввода
def take_input(player_token):
	while True:
		value = input("В какое поле поставить: " + player_token + " ? ")
		if not (value in "123456789"):
			print("Неверный ввод. Повторите.")
			continue
		value = int(value)
		if str(board[value - 1]) in "XO":
			print("Это поле уже занято")
			continue
		board[value - 1] = player_token
		break


# функция проверки выигрышной комбинации
def win_func():
	wins_cord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8)]
	for i in wins_cord:
		if board[i[0]] == board[i[1]] == board[i[2]]:
			return board[i[0]]
	return False


# основная функция программы
def main():
	counter = 0
	while True:  # цикл очередности игроков
		draw_board()
		if counter % 2 == 0:
			take_input("X")
		else:
			take_input("O")
		if counter > 3:  # проверка на выигрышную комбинацию
			winner = win_func()
			if winner:  # условие определения победителя
				draw_board()
				print(winner, "Выиграл")
				break
		counter += 1
		if counter > 8:  # условие при котором будет ничья
			draw_board()
			print("Победила дружба")
			break


main()
