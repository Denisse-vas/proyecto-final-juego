# Mostrar Tablero
def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

# Lógica ingresar movimiento
def enter_move(board):
	ok = False	# suposición falsa - la necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento: ")
		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X']
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar 'O' al cuadro seleccionado
		

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío

display_board(board)