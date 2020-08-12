#NO BORRE ESTE CODIGO
import os

colors = [('negro','\033[0;37;48m'),
           ('blanco','\033[0;37;47m'),
           ('rojo','\033[0;37;41m'),
           ('verde','\033[0;37;42m'),
           ('amarillo','\033[0;37;43m'),
           ('azul','\033[0;37;44m'),
           ('magenta','\033[0;37;45m'),
           ('celeste','\033[0;37;46m')]

canvas= [
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco']
]

native='\033[m'
#COMIENCE A PROGRAMAR ABAJO DE ESTA LINEA (NO BORRE EL CODIGO ANTERIOR)

#Muestra el lienzo en pantalla
def show_canvas(canvas, colors):

	printable_canvas = []
	number_of_row = 0
	number_of_column = len(canvas[0])
	number_of_column_string = ""

	#obtencion del largo de 
	for number in range(1, number_of_column+1):
		if len(number_of_column_string) > 17:
			number_of_column_string += str(number)
		else:
			number_of_column_string += str(number)+" "
	
	#creacion de una lista con valores printeables
	for row in canvas:
		printable_canvas.append([])

		for color in row:
			for color_name, color_code in colors:

				if color == color_name:
					printable_canvas[number_of_row].append(color_code+"  "+native)

		number_of_row += 1
	
	#print de las filas y columnas de la lista creada
	print("  ", number_of_column_string)
	for i in range(number_of_row):
		printable_row = ""
		for c in range(number_of_column):
			printable_row += str(printable_canvas[i][c])
		if i < 9:
			print(str(i+1)+" ", printable_row)
		else:
			print(i+1, printable_row)

def deep_copy(list_to_copy):
	new_data = []
	deeped_copy_list = []
	for data in list_to_copy:
		new_data = list(data)
		deeped_copy_list.append(new_data)

	return deeped_copy_list


#seteo de unas variables
number_of_column = len(canvas)
number_of_row = (len(canvas[0]))
end_program = False
white_canvas = deep_copy(canvas)
user_canvas = deep_copy(canvas)
is_data_saved = False
character_list = "qwertyuiopasdfghjklñzxcvbnm,.-<>´+}{]['¿!|¬°#$%&/()=?¡@*~^`_;:s"+'"'+"\\"
#inicio del bucle del programa
while not end_program:

	user_input = 0

	#menu de acciones con validacion de datos
	while user_input != "1" and user_input != "2":
		if not is_data_saved:
			print("1)Crear nuevo dibujo")
		else:
			print("1)Continuar dibujo")
		print("2)Salir")
		user_input = input("Seleccione una opcion: ")
		if user_input != "1" and user_input != "2":
			print("¡Opcion inválida! Ocupa 1 o 2")

	#Nuevo dibujo o continuar dibujo
	if user_input == "1":
		back_to_menu = False
		while not back_to_menu:

			user_input_tool = 0
			
			#despliegue del lienzo en pantalla
			show_canvas(user_canvas, colors)

			#menu de herramientas con validacion de datos
			while user_input_tool != "1" and user_input_tool != "2" and user_input_tool != "3":
				print("1)Dibujar un punto")
				print("2)Pintar todo el lienzo")
				print("3)Volver al menú principal")
				user_input_tool = input("Seleccione una herramienta: ")
				if user_input_tool != "1" and user_input_tool != "2" and user_input_tool != "3":
					print("¡Opcion inválida! Ocupa 1 o 2")

			#dibujar un punto
			if user_input_tool == "1":

				#validacion de fila
				row_verification = False
				while not row_verification:
					row = input("Ingrese fila: ").lower()
			
					if len(row) == len(str(number_of_column)):
						if row[0] in character_list:
							print("Utiliza un número y no uses caracteres extraños")
						elif int(row) in range(1,len(user_canvas)+1):
							row_verification = True
						else:
							print("Selecione una fila dentro de los limites 1-"+str(len(user_canvas))+":" )
					else:
						print("Selecione una fila dentro de los limites 1-"+str(len(user_canvas))+":" )
				#validacion de columna
				column_verification = False
				while not column_verification:
					column = input("Ingrese columna: ").lower()
					
					if len(column) == len(str(number_of_row)):
						if column[0] in character_list:
							print("Utiliza un número y no uses caracteres extraños")
						elif int(column) in range(1,len(user_canvas[0])+1):
							column_verification = True
						else:
							print("Selecione una columna dentro de los limites 1-"+str(len(user_canvas[0]))+":" )
					else:
						print("Selecione una columna dentro de los limites 1-"+str(len(user_canvas[0]))+":" )
				
				#validacion de color
				color_verification = False
				while not color_verification:
					color = input("Ingrese color: ").lower()
					for color_name, _ in colors:
						if color_name == color:
							color_verification = True
					if not color_verification:
						print("El color fue mal ingresado o no esta disponible" )
						print("Por favor seleccione uno a continuacion: ")
						for color_name, _ in colors:
							print(color_name)

				#cambio de color en la matriz
				user_canvas[int(row)-1][int(column)-1] = color

			elif user_input_tool == "2":
				color_verification = False
				while not color_verification:
					color = input("Ingrese color: ").lower()
					for color_name, _ in colors:
						if color_name == color:
							color_verification = True
					if not color_verification:
						print("El color fue mal ingresado o no esta disponible" )
						print("Por favor seleccione uno a continuacion: ")
						for color_name, _ in colors:
							print(color_name)

				for a in range(len(user_canvas)):
					for c in range(len(user_canvas[a])):
						user_canvas[a][c] = color

			#volver al menu
			else:
				#guardado del lienzo
				input_verification = False
				while not input_verification:
					save_canvas = input("Quieres guardar el lienzo?[Si/No/S/N]: ").lower()
					
					#la lista ya esta modificada, por lo que solo saldra del bucle
					if save_canvas in "si" and save_canvas != "" and save_canvas != "i":
						input_verification = True
						is_data_saved = True
						print("Dibujo guardado")
					
					#seteo del lienzo en blanco
					elif save_canvas in "no" and save_canvas != "" and save_canvas != "o":
						input_verification = True
						is_data_saved = False
						print("Dibujo descartado")
						user_canvas = white_canvas
					
					else:
						print("Datos mal ingresados")
						


				back_to_menu = True

	#terminar programa
	else:
		end_program = True

