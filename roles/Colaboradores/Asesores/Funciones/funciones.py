import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','.')))


class consultar_codigo_producto :
  
  def consultar_codigo():
    while True:
      print('\n\t----- Consulta por codigo del Producto -----\n')
      id_producto = input('Ingrese el ID del producto (o n para salir) : ')
      
      if id_producto.lower() == 'n':
        salir.salir_sistema()
        break
      
      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              if id_producto == campos[0]:
                  print('\n\t► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Articulo : {campos[1]}')
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
      if not bandera:
        print('\n► No encontrado.')


class consultar_descripcion_producto :

  def consultar_descripcion():
    while True:
      print('\n\t----- Consulta por descripcion del Producto -----\n')
      descripcion_producto = input('Ingrese la descripcion del producto (o n para salir) : ')

      if descripcion_producto.lower() == 'n':
        salir.salir_sistema()
        break

      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              if descripcion_producto.lower() in campos[1].lower():
                  print('\n\t► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Articulo : {campos[1]}')
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
                  print()
      if not bandera:
        print('\n► No encontrado.')


class consultar_por_categoria :
  
  def consultar_categoria() :
    while True:
      # IMPRIMIR LAS CATEGORIAS.txt
      print()
      bandera = False
      with open('Recepcion/Categorias/categorias.txt', 'r', encoding='utf-8', errors='ignore') as file:
        print('CODIGO \t\tCATEGORIA')
        for linea in file:
          campos = linea.strip().split(",")
          print(f'{campos[0]} \t\t{campos[1]}')
          bandera = True

      categoria_producto = input('\n> Ingrese la categoria (o n para salir) : ') # PREGUNTAR LA CATEGORIA
      if categoria_producto.lower() == 'n':
        salir.salir_sistema()
        break
      
      # Imprimir las series.txt
      with open('Recepcion/Series/series.txt', 'r', encoding='utf-8', errors='ignore') as file:
        print('\nCODIGO \t\tSERIE')
        for linea in file:
          campos = linea.strip().split(",")
          if categoria_producto == campos[2]:
            print(f'{campos[0]} \t\t{campos[1]}')
            bandera = True

      if not bandera:
        print('\n► No encontrado.')

      # Ingresar la serie
      serie_producto = input('\n> Ingrese la serie (o n para salir) : ') # PREGUNTAR LA SERIE
      if serie_producto.lower() == 'n':
        salir.salir_sistema()
        break

      # Imprimir los productos que coinciden con la categoria y serie
      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
        print('\nCODIGO \t\tARTICULO \t\t\t\tSTOCK \t\t\tPRECIO')
        for linea in file:
          campos = linea.strip().split(",")
          if serie_producto == campos[2] :
            print(f'{campos[0]} \t\t{campos[1]} \t\t{campos[3]} \t\t\t{campos[4]}')
            bandera = True

      if not bandera:
        print('\n► No encontrado.')
      
      print()
      pregunta = input('¿Desea realizar otra consulta? (si/no): ').strip().lower()
      if pregunta == 'si':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
      elif pregunta == 'no':
        salir.salir_sistema()
        break
      else:
        consultar_por_categoria.consultar_categoria()

class consultar_stocks_bajos :

  def consultar_stocks():
    while True:
      print('\n\t----- Consulta de Stocks Bajos -----\n')
      stock_bajo = input('Ingrese el stock bajo (o n para salir) : ')

      if stock_bajo.lower() == 'n':
        salir.salir_sistema()
        break

      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
          for linea in file:
              campos = linea.strip().split(",")
              if int(campos[3]) <= int(stock_bajo):
                  print('\n► Encontrado...')
                  print(f'Codigo : {campos[0]}')
                  print(f'Nombre : {campos[1]}')
                  print(f'Precio : Q {campos[4]}')
                  print(f'Stock : {campos[3]}')
                  bandera = True
                  print()
                  
      if not bandera:
        print('\n► No encontrado.')


class salir :

  def salir_sistema():
    os.system('cls' if os.name == 'nt' else 'clear')
    from asesor1 import Menu_Asesor    
    Menu_Asesor()
    pass