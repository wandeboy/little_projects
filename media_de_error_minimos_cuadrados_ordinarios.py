import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston


def ask_for_points():
  #puntos en la recta
  axis_x_data = []
  axis_y_data = []


  #peticion de los puntos en la recta
  while True:
    user_input = input("ingrese coordenadas (x, y), ponga start para continuar: ").lower()
    if user_input == "start" or user_input == "s":
      break
    try:
      x_point = float(user_input[user_input.index("(")+1:user_input.index(",")])
      y_point = float(user_input[user_input.index(",")+1:-1])
    except ValueError:
      x_point = float(user_input[user_input.index("(")+1:user_input.index(",")])
      y_point = float(user_input[user_input.index(",")+2:-1])
    except:
      print("Datos mal ingresados, ingreselos de nuevo")
      continue
    axis_x_data.append(x_point)
    axis_y_data.append(y_point)

  return axis_x_data, axis_y_data


def evalue_in_x(formula):
  while True:
    user_input = input('ingrese el valor de x a evaluar,\
 para terminar escriba "exit": ').lower()
    if user_input == "exit" or user_input == "e":
      break
    try:
      y_point = formula[0] + formula[1] * float(user_input)
      print(y_point)
    except:
      print("datos mal ingresados")


def how_many_decimals(axis_x_data):
  average = 0
  for i in axis_x_data:
    average += len(str(np.ceil(i)))-len(str(np.ceil(i)))-1

  return int(np.rint(np.array(average/length_row_matrix)))


#carga de libreria con datos de prueba
boston = load_boston()

#seteo de los puntos con la libreria anterior
axis_x_data = boston.data[:, 5]
axis_y_data = boston.target


"""
axis_x_data, axis_y_data = ask_for_points()
"""

#largo de la matriz de x, para luego poder sumarle el intersecto
length_row_matrix = len(axis_x_data)

#convercion de las listas a matricez
x = np.array(axis_x_data)
y = np.array(axis_y_data)

#construcion del plano, con transparencia de los puntos 70%
plt.scatter(x, y, alpha=0.3)

# se añade una fila de 1nos para obtener el intersecto
x = np.array([np.ones(length_row_matrix), x]).T

#formula de (MCO) 
alpha = np.linalg.inv(x.T @ x) @ x.T @ y

#construccion de la recta
plt.plot([np.floor(np.min(axis_x_data)), np.ceil(np.max(axis_x_data))],
         [alpha[0] + alpha[1] * np.floor(np.min(axis_x_data)),
          alpha[0] + alpha[1] * np.ceil(np.max(axis_x_data))], c="red")

#impresion de la grafica
plt.show()

#promedio de decimales ocupados en los datos
average_decimal= how_many_decimals(axis_x_data)

# retorno de pendiente y intersecto
print("recta con pendiente {} y intersecto {}"
.format(alpha[1], alpha[0]))

#pregunta si quiere evaluar en la funcion
evalue_in_x(alpha)

