import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from pruebas import producto

with open("productos.txt", "r") as file:
    row = file.readlines()
    row = [line.strip().split(',') for line in row]
    print(row)  # Acceder a las listas por indices.