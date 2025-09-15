
import random

# Lista de alumnos
alumnos = [
    "Lautaro Agustín Aguero",
    "Mateo Alejo Algañaraz",
    "Yoselie Aquino",
    "Santiago Facundo Barretto",
    "Ayrton Calderon",
    "María Belén Calvo García",
    "Nicolas Exequiel Carchano",
    "Sergio Joaquin Chiarello Ghilardi",
    "Santino Cárdenas Valls",
    "Octavio Agustin Fiore Montivero",
    "Bruno Fiouchetta",
    "Braian Leandro Flores Marin",
    "Agustina Luz Fontagnol",
    "Maximo Mateo Franco",
    "Facundo Adrian Gomez Romero",
    "Marcelo Hernán Gonzalez",
    "Genaro Guillot",
    "Camilo Javier Illanes Donoso",
    "Matias Nicolas Limina Nuñez",
    "Federico Alejandro Lopez",
    "Jeremías Daniel Luzuriaga",
    "Santino Mantineo",
    "Ezequiel Menéndez",
    "Nicolás Monjelardi",
    "Joel Nicolas Moreno",
    "Nicolás Uriel Moron Gutierrez",
    "Joaquín Morán",
    "Santino Naldini Sosa",
    "Andres Victor Novello",
    "Joseph Oliveros",
    "Santiago Javier Ontivero Parlade",
    "Roberto Paul Paiva",
    "Matías Pereyra",
    "Gianella Sol Peña",
    "Leonel Lautaro Ponce De Leon Martinez",
    "Cristian Nestor Rodriguez Martinez",
    "Ignacio Martín Rodríguez",
    "Rafael Ignacio Ruiz Guiñazú Puebla",
    "Florencia Santos",
    "Marcelo Scherer Huf",
    "Martina Guadalupe Suarez",
    "Elias Emanuel Tello",
    "Agustina Luz Fontagnol"
]

# Mezclar la lista
lista_final_alumnos = alumnos[:]  # copiamos la lista
random.shuffle(lista_final_alumnos)

# Cantidad de grupos (4 alumnos por grupo)
tamaño_grupo = 4
cantidad_grupos = (len(lista_final_alumnos) + tamaño_grupo - 1) // tamaño_grupo

# Crear matriz vacía
matriz_grupo = [[] for _ in range(cantidad_grupos)]

# Llenar matriz con índices aleatorios
llenar_matriz_aleatoria_indice = 0
for alumno in lista_final_alumnos:
    matriz_grupo[llenar_matriz_aleatoria_indice].append(alumno)
    llenar_matriz_aleatoria_indice = (llenar_matriz_aleatoria_indice + 1) % cantidad_grupos

# Mostrar matriz de grupos
for i, grupo in enumerate(matriz_grupo, 1):
    print(f"Grupo {i}: {grupo}")