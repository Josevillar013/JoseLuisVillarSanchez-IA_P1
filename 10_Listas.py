# Lista de colores
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]

# Intentamos acceder a una posición incorrecta o fuera del rango
color_pos_10 = colores[10]  

# Crear una lista con los valores en posiciones incorrectas
nueva_lista = [None] * 5

nueva_lista[6] = "uno"  # la lista tiene solo 5 posiciones, de 0 a 4

nueva_lista[2] = "dos"
nueva_lista[1] = "tres"
nueva_lista[0] = "cuatro"
nueva_lista[3] = "cinco"

print(nueva_lista)
