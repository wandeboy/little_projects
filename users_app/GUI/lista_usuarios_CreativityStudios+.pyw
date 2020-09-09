import pickle, pyglet
from tkinter import *
pyglet.font.add_file('Dreamland.otf')

'''
agregar la interfaz graficas con tkinter
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
	data_file = open("data.pickle", "rb")
	unplicke_data = pickle.load(data_file)
	data_file.close()
	tokens_list = []

	for client in unplicke_data:
		tokens_list.append(client[0])

	if len(tokens_list) == 0:
		return "A000"

	letter,n1,n2,n3 = tuple(tokens_list[-1])
	n = int(n1)+int(n2)+int(n3)
	n += 1

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
	data_file = open("data.pickle", "rb")
	unplicke_data = pickle.load(data_file)
	data_file.close()

	unplicke_data.append([token, str(name), dict()])

	data_file = open("data.pickle", "wb")
	pickle.dump(unplicke_data, data_file)
	data_file.close()	
	
	print("Cliente creado exitosmanete")

	yes_no = input("Quieres agregarle una cuenta al cliente?[S/N]: ")

	if yes_no.upper() == "S":
	 	add_data_to_client(token)
	else:
	 	print("No se agregara un dato.")

#completa
def show_clients():
	data_file = open("data.pickle","rb")
	unplicke_data = pickle.load(data_file)
	data_file.close()
	for client in unplicke_data:
		name = client[1]
		print(name)

#completa
def add_data_to_client(token):
	accountant = 0
	data_file = open("data.pickle","rb")
	unplicke_data = pickle.load(data_file)
	data_file.close()

	for client in unplicke_data:
		token_in_file = client[0]
		if token == token_in_file:
			client_data = client
			index = accountant
		accountant += 1

	data_name = input("Que quieres agregar a "+str(client_data[1])+": ")
	username = input("Ingresa el usuario: ")
	password = input("Ingresa la contraseña: ")

	# token;name;{data_name:(username,password)}
	dictionary = client_data[2]
	if data_name in dictionary:
		print(data_name, "ya existe, por favor guardalo con otro nombre")
		return
	else:
		dictionary[data_name] = (username, password)

	data_file = open("data.pickle", "wb")
	pickle.dump(unplicke_data, data_file)
	data_file.close()

#en progreso
def search_client():
	name_to_search = input("Que cliente buscas?: ")
	token = []
	data_file = open("data.pickle","rb")
	unplicke_data = pickle.load(data_file)
	data_file.close()

	for client in unplicke_data:
		name = client[1]
		if name.upper() == name_to_search.upper():
			token.append(client[0])

	if len(token) == 0:
		print("no se encontro a", name)
	elif len(token) > 1:
		print("se encontraton", len(token), name)
		client = []
		for i in range(len(token)):
			client.append(show_data(token[i]))
	else:
		print("Se encontro a", name)
		client = show_data(token[0])
		account = input("que cuenta quieres ver?: ")



def show_data(token):
	data_file = open("data.pickle","rb")
	unplicke_data = pickle.load(data_file)
	data_file.close()

	for client in unplicke_data:
		if token == client[0]:
			match_client = client
			for accounts in client[2]:
				print(accounts)

	return match_client



if __name__ == "__main__":

	try:
		pickle_file = open("data.pickle","rb")
		pickle_data = pickle.load(pickle_file)
		pickle_file.close()
		if type(pickle_data) != type(list()):
			pickle_file = open("data.pickle","wb")
			empty_list = []
			pickle.dump(empty_list, pickle_file)
			pickle_file.close()

	except:
		pickle_file = open("data.pickle","wb")
		empty_list = []
		pickle.dump(empty_list, pickle_file)
		pickle_file.close()

	root = Tk()
	root.title("CreativityStudios+'s book")
	root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.png'))
	root.config(bg="white")

	frame = Frame(root, width="650", height="500", bg="#2af6dd")
	frame.pack(expand=1, fill="both")

	Label(frame, text="Prueba texto", fg="black", bg="#2af6dd", font="Dreamland, Regular").place(x=100, y=200)

	root.mainloop()

