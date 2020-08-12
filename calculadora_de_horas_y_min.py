def hour_and_minute_calculator():
	validation = False

	while not validation:
		first_user_hours = input("Horas: ")
		first_user_minutes = input("Minutos: ")
 
		second_user_hours = input("Horas: ")
		second_user_minutes = input("Minutos: ")

		try:
			a = int(first_user_hours+"0"+first_user_minutes)
			b = int(second_user_hours+"0"+second_user_minutes)
			validation = True
		except:
			print("datos mal ingresados")
			validation = False
	
	value = str(a + b)

	while int(value[-2:]) > 60 or value[-3] != "0":
		str(int(value)+940)

	return value[:-3], value[-2:]

print(hour_and_minute_calculator())
