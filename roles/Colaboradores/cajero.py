import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pruebas import producto

producto()

with open("productos.txt", "r") as file:
    print(file.read())