import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','.')))
# from asesor1 import Menu_Asesor


class asesor :
  pass

class consultar_codigo_producto :
  
  def consultar_codigo():
    while True:
      print('\n\t----- Consulta por codigo del Producto -----\n')
      id_producto = input('Ingrese el ID del producto (o n para salir) : ')
      
      if id_producto.lower() == 'n':
        print('→ Gracias por usar el sistema. Saliendo...')
        break
      
      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              if id_producto == campos[0]:
                  print('► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Nombre : {campos[1]}')
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
      if not bandera:
        print('► No encontrado.')


class consultar_descripcion_producto :

  def consultar_descripcion():
    while True:
      print('\n\t----- Consulta por descripcion del Producto -----\n')
      descripcion_producto = input('Ingrese la descripcion del producto (o n para salir) : ')

      if descripcion_producto.lower() == 'n':
        print('→ Gracias por usar el sistema. Saliendo...')
        break

      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              if descripcion_producto.lower() in campos[1].lower():
                  print('► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Nombre : {campos[1]}')
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
      if not bandera:
        print('► No encontrado.')


class consultar_por_categoria :
  
  def consultar_categoria() :
    while True:
      print('\n\t----- Consulta por categoria del Producto -----\n')
      categoria_producto = input('Ingrese la categoria del producto (o n para salir) : ')

      if categoria_producto.lower() == 'n':
        print('→ Gracias por usar el sistema. Saliendo...')
        break

      bandera = False
      # Archivo productos.txt
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              
              if categoria_producto.lower() in campos[2].lower():
                  print('► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Nombre : {campos[1]}')

                  # Archivo categorias.txt
                  with open('Recepcion/Categorias/categorias.txt', 'r', encoding='utf-8', errors='ignore') as categorias:
                    for categoria in categorias:
                      categoria_auxiliar = categoria.strip().split(",")
                      if categoria_auxiliar[0] == campos[2]:
                        print(f'Categoria : {categoria_auxiliar[1]}')
                      
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
                  print()
                  
      if not bandera:
        print('► No encontrado.')


class consultar_stocks_bajos :

  def consultar_stocks():
    while True:
      print('\n\t----- Consulta de Stocks Bajos -----\n')
      stock_bajo = input('Ingrese el stock bajo (o n para salir) : ')

      if stock_bajo.lower() == 'n':
        # Menu_Asesor()
        break

      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              if int(campos[3]) <= int(stock_bajo):
                  print('► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Nombre : {campos[1]}')
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
                  print()
                  
      if not bandera:
        print('► No encontrado.')


class salir :

  def salir_sistema():
    pass
    # Menu_Asesor()