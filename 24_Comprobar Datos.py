colores = input('Introduce un color:\n')
tupla_colores = ('rojo', 'azul', 'verde', 'amarillo')

if colores in tupla_colores[0]:
	print('El color rojo esta admitido')
elif colores in tupla_colores[1]:
	print('El color azul esta admitido')
elif colores in tupla_colores[2]:
	print('El color verde esta admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo esta admitido')
else:
	print('Color no admitido')
 