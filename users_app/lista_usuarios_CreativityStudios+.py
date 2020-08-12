import pickle
'''
ocupar pickle y terminar la funcion de modificacion de clientes
'''

def main():
	while True:

		print("1)Añadir Cliente")
		print("2)Buscar Cliente")
		print("3)Mostrar Todos Los Clientes")

		user_input = input("¿Que quieres hacer?: ")

		if user_input == "1":
			add_client()
		elif user_input == "2":
			search_client()
		elif user_input == "3":
			show_clients()
		else:
			break

#completa
def token_gen():
	token_file = file("data.pickle")
	tokens_list = []

	for line in token_file:
		tokens_list.append(line.strip().split(";")[0])

	token_file.close()

	if len(tokens_list) == 0:
		return "A000"

	letter,n1,n2,n3 = tuple(tokens_list[-1])
	n = int(n1)+int(n2)+int(n3)
	n =+ 1

	if n > 999:
		letter = ord(letter)
		token = chr(letter+1)+"000"
	elif n < 10:
		token = letter+"00"+str(n)
	elif n < 100:
		token = letter+"0"+str(n)
	else:
		token = letter+str(n)

	return token

#Completa
def add_client():
	name = input("Nombre del Cliente: ")
	token = token_gen()
	data_file = file("data.pickle")
	file_data_list = []

	for line in data_file:
		file_data_list.append(line)
	data_file.close()

	file_data_list.extend(list(token+";"+str(name)+"\{}"+"\n"))

	data_file = open("data.pickle", "w")
	data_file.writelines(file_data_list)
	data_file.close()	
	
	print("Cliente creado exitosmanete")

"""
  yes_no = input("Quieres agregarle un dato al cliente?[S/N]: ")
  
  if yes_no.upper() == "S":
    add_data_to_client(name)
  else:
    print("No se agregara un dato.")
"""

#completa
def show_clients():
	data_file = file("data.pickle")
	for line in data_file:
		name = line.strip().split(";")[1]
		print(name)
	data_file.close()


def add_data_to_client(token):
	file_data_list = []
	accountant = 0
	data_file = file("data.pickle")

	for line in data_file:
		file_data_list.append(line)
		token_in_file = line.strip().split(";")[0]
		if token == token_in_file:
			client_data = line.strip().split(";")
			index = accountant
		accountant += 1
	data_file.close()

	data_name = input("Que quieres agregar a "+str(client_data[1])+":")
	username = input("Ingresa el usuario: ")
	password = input("Ingresa la contraseña: ")

	# token;name;{data_name:(username,password)}
	dictionary = client_data[2]
	if data_name in dictionary:
		print(data_name, "ya existe, por favor guardalo con otro nombre")
	else:
		dictionary[data_name] = (username, password)

	data = [token, name, str(dictionary)]
	file_data_list[index] = new_data

	data_file = open("data.pickle", "w")
	data_file.writelines(file_data_list)
	data_file.close()


def search_client():
	name_to_search = input("Que cliente buscas?: ")
	data_file = file("data.pickle")
	for line in data_file:
		name = line.strip().split(";")[0]
	if name == name_to_search:
		print("Se encontro a",name)
		data = line.strip.split(";")
		for things in data:
			print(things)
	data_file.close()


if __name__ == "__main__":
	main()
