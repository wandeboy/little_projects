from random import randint, shuffle
from time import sleep

class Create_game:
	def __init__(self,):
		self.__deck = Deck()
		self.__user = Player(input("Cual es tu nombre?: "))
		self.__player = Player()


	def __game_end(self, user, player):
		if self.__deck.how_many_cards_are_left() == 0 or len(player.show_hand()) == 0 or len(player.show_hand()) == 0:
			return True
		else:
			return False

	def __choose_action(self, aux_var, player):
		if type(aux_var) == type(str()):
			aux_var = aux_var.replace(" ","")
		if aux_var == "2" or aux_var == "3":
			return True
		elif aux_var == "1" or aux_var == None:
			print("Tu mano:", player.show_hand())
			sleep(1)
			return False
		elif aux_var == "4":
			print("En la mesa hay un", self.__deck.show_the_table())
			return False
		else:
			aux_var = input("por favor elije un numero entre 1 y 4: ")
			return self.__choose_action(aux_var, player)

	def __turn(self, player):
		#Check if are a winner
		if self.__deck.how_many_cards_are_left() == 0 or len(player.show_hand()) == 0:
			flag = player
			return True
		#Bot play	
		if player == self.__player:
			sleep(1)
			index = 0
			print("Es el turno de", player.get_name())
			hand_list = player.show_hand()
			for tuple_card in hand_list:
				card = player.get_hand()[index]
				if self.__deck.is_valid(card):
					sleep(1)
					print("El contricante jugo un", tuple_card)
					player.play_card(index)
					self.__deck.update_table(card)
					return
				index += 1
			sleep(1)
			print("El contricante robo del maso")
			card = self.__deck.give_card()
			player.pick_a_card(card)

		#User play
		else:
			aux_var = None
			print(player.get_name(), "es tu turno")
			sleep(1)
			print("En la mesa hay un", self.__deck.show_the_table())
			sleep(1)
			while not self.__choose_action(aux_var, player):
				print("Que quieres hacer?")
				print("1)Mostrar mano")
				print("2)Sacar carta")
				print("3)Botar carta")
				print("4)Ver mesa")
				aux_var = input("Elije un numero entre 1-4: ")
			if aux_var == "2":
				card = self.__deck.give_card()
				if player.pick_a_card(card):
					print("Carta", card.get_data(), "Tomada")
			else:
				player.show_hand()
				print("info: la posicion parte contando DESDE el 0")
				card = player.play_card(input("En que posicion esta la carta a jugar?: "))
				if card == None:
					return True
				elif not self.__deck.is_valid(card):
					print("La carta", card.get_data(), "no es valida")
					player.pick_a_card(card)
					print("Pierdes tu turno y ganas una carta")
					card = self.__deck.give_card()
					if player.pick_a_card(card):
						print("Carta", card.get_data(), "Tomada")
				else:
					print("jugaste la carta", card.get_data())
					self.__deck.update_table(card)

		return False

#completar
	def __who_win(self):
		pass

	def start_game(self):
		self.__user.inicializate_hand(self.__deck)
		self.__player.inicializate_hand(self.__deck)

		while not self.__game_end(self.__user, self.__player):
			if self.__turn(self.__user):
				flag = self.__user
				break
			if self.__turn(self.__player):
				flag = self.__player
				break
		self.__who_win()


class Card:
    # Una carta tiene un valor entre 1 y 10, y un
    # color (rojo, amarillo, azul o verde)
    def __init__(self, value, colour):
        self.__value = value
        self.__colour = colour
        
    # Retorna una tupla con los datos de la
    # carta (valor, color)
    def get_data(self):
        return (self.__value,self.__colour)


class Deck():

	def __init__(self):
		self.__deck = []
		__colours = ["Amarillo", "Rojo", "Azul", "Verde"]
		__numbers = [i for i in range(1,11)]
		for colour in __colours:
			for number in __numbers:
				self.__deck.append(Card(number,colour))
		shuffle(self.__deck)
		self.__table = self.__deck.pop(randint(0,len(self.__deck)))

	def how_many_cards_are_left(self):
		return len(self.__deck)

	def give_card(self):
		card_to_give = self.__deck.pop(randint(0,len(self.__deck)-1))
		return card_to_give

	def show_the_table(self):
			return self.__table.get_data()

	def update_table(self, new_card):
		self.__table = new_card

	def is_valid(self, card):
		return (self.__table.get_data()[1] == card.get_data()[1] or self.__table.get_data()[0] == card.get_data()[0])
        

class Player:

    def __init__(self, name="José"):
        self.__name = name
        self.__hand = []

    # Retorna el nombre del jugador
    def get_name(self):
        return self.__name

    def get_hand(self):
    	return self.__hand

    def inicializate_hand(self, deck):
    	for i in range(7):
    		self.__hand.append(deck.give_card())

    # Retorna una lista de tuplas (valor, color) de las cartas en la mano
    def show_hand(self):
        cards = []
        for c in self.__hand:
            cards.append(c.get_data())
        return cards

    def play_card(self, card_position):
	    try:
	    	card_position = int(card_position)
	    	if len(self.__hand) > card_position and len(self.__hand) != 0:
	    		return self.__hand.pop(card_position)
	    	elif card_position < 0:
	    		print("Coloca numeros positivos")
	    		card_position = input("posicion: ").replace(" ","")
	    		return self.play_card(card_position)
	    	elif card_position > len(self.__hand):
	    		print("Tienes menos cartas que la posicion dada")
	    		card_position = input("posicion: ").replace(" ","")
	    		return self.play_card(card_position)
	    	else:
	        	return None
	    except ValueError:
	    	print("Por favor coloca solo el numero de la posicion")
	    	card_position = input("posicion: ").replace(" ","")
	    	return self.play_card(card_position)
	    	        
    #Agrega una carta a la mano
    def pick_a_card(self, card):
        self.__hand.append(card)
        return True
    
    #COMPLETAR: Debe sumar el valor de las cartas en la mano
    # y retornar la suma total
    def actual_score(self):
    	score = sum(show_hand())
    	return score

    
######### PROGRAMA PRINCIPAL ######
#'IMPLEMENTE AQUI LA LOGICA DEL JUEGO UNO'
	
game = Create_game()
game.start_game()

"""
'Crear dos jugadores, con sus respectivas manos de 7 cartas
' (recuerde los valores y colores validos para las cartas en este juego)
'Crear un mazo como una lista de 10 cartas
'La primera carta del mazo pasa a ser el pozo de descarte

'Ciclo principal del juego
'Repetir mientras haya cartas en el pozo o bien no hay ganador/a
    'Imprimir la carta que esta encima en el pozo
    'Imprimir el nombre de la persona que le toca jugar
    'Preguntar si desea tomar una carta del mazo o botar una carta de su mano
        'Si desea tomar la carta del mazo, sacar la carta del mazo y agregarla a la mano del jugador/a
            'Si la nueva carta cumple con las reglas, botarla al pozo
        
        'Si desea botar una carta
            'Preguntar la carta que desea botar y chequear si cumple las reglas
                'Si cumple las reglas, sacar la carta de la mano y ponerla encima del pozo
                'Si no cumple, pierde el turno
                
    'Chequear si hay ganador/a o si el pozo está vacio
        'Si hay ganador, mostrar un mensaje y terminar el juego
        'Si el pozo está vacío, chequear quien tiene menor puntaje y mostrar un mensaje indicandolo Mostrar un mensaje
"""