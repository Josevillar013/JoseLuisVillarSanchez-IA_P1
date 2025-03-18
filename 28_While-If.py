# Valor inicial de x
x = 0

# while se ejecuta hasta menor o igual que 30
while x <= 30:
	x += 1  # incrementos de 1

	# if para saltar ejecuciones del bucle
	if x == 4 or x == 6 or x == 10:
		print('Se salto el valor ', x, ' de x')
		continue

	# if para romper la ejecuci�n del bucle
	if x == 15:
		print('Se rompio la ejecucion del bucle cuando x valia: ', x)
		break

	# imprime los resultados que no se corresponden a ninguno de los if
	print(x)
 