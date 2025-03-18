#¿que color esta en la posicion 3 de la lista?

colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]

color_pos_3 = colores[3]
print(color_pos_3)

#¿en que posicion se encuentra el color "rojo"?

pos_rojo = colores.index("rojo")
print(pos_rojo)

#¿en que posicion se encuentra el color "rosa"?

pos_rosa = colores.index("rosa")
print(pos_rosa)

#Para crear una lista que contenga los valores "uno", "dos", "tres", "cuatro" y "cinco" en las posiciones indicadas

nueva_lista = [None] * 5  # Creamos una lista de 5 elementos vacíos

nueva_lista[4] = "uno"
nueva_lista[1] = "dos"
nueva_lista[0] = "tres"
nueva_lista[3] = "cuatro"
nueva_lista[2] = "cinco"

print(nueva_lista)

