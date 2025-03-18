def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marron', 'naranja')

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco esta mal.')

colores('rojo', 'azul')
