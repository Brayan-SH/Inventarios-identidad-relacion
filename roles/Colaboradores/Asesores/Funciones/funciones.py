import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','.')))


class asesor :
  pass

class consultar_codigo_productos :
  
  def consultar_codigo_producto(self):
    
    while True:
          print('\n\t----- Consulta por codigo del Producto -----\n')
          id_producto = input('Ingrese el ID del producto (o n para salir) : ')
          
          if id_producto.lower() == 'n':
              break
            
          else :
            bandera = False
            with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
                for linea in file:
                    campos = linea.strip().split(",")
                    if id_producto == campos[0]:
                        print('► Encontrado...')
                        print(f'Codigo : {campos[0]}')
                        print(f'Nombre : {campos[1]}')
                        print(f'Precio : {campos[2]}')
                        print(f'Stock : {campos[3]}')
                        bandera = True
            if not bandera:
                print('► No encontrado.')
                
            pregunta = input('\n¿Desea volver al menú principal? (s/n): ').lower()
            match pregunta:
              case 's':
                self.consultar_codigo_producto()
              case 'n':
                print('→ Gracias por utilizar el sistema.')
                break
              case _:
                print('Opción no válida. Regresando al menú principal.')
                self.consultar_codigo_producto()
            print()


class consultar_descripcion_producto :
  pass


class consultar_por_categoria :
  pass


class consultar_stocks_bajos :
  pass
