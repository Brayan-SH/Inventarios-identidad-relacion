import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class vender :
    
    def vender() :
        with open("Recepcion/Series/series.txt", "r", encoding="utf-8", errors="ignore") as file:
            lineas = file.readlines()
            lineas = [line.strip().split(',') for line in lineas]
            print(lineas)  # Acceder a las listas por indices.


# with open("Recepcion/lineas/lineas.txt", "r", encoding="utf-8", errors="ignore") as file:
#     lineas = ''
#     lineas = [line.strip().split(',') for line in lineas]
#     print(lineas)  # Acceder a las listas por indices.