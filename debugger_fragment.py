axis_x_data = [0, 1, 1.99, 3.01, 4.03, 5.03, 6.04, 7.06, 8.05, 9.06, 10.08, 11.09, 12.09, 13.1, 14.1, 15.12, 16.13]

average = 0
for i in axis_x_data:
  try:
    decimal = str(float(i%int(i)))
  except ZeroDivisionError:
    decimal = "0.0"
  average += len(str(decimal))-2

print(average)
