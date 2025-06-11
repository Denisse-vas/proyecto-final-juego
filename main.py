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
	
# Lógica ver campos vacios
def make_list_of_free_fields(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # itera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free
		

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True # ¿De quien es turno ahora?

display_board(board)