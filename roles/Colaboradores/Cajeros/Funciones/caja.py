from datetime import datetime 
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','.')))

class MetodosCajero :
  
  def Vender() :

    MetodosCajero.Limpiar()
    print(f'------- VENDER  -------')

    print()
    articulo = input('Ingrese la descripcion o codigo del articulo (o n para salir) : ')
    if articulo.lower() == 'n' or articulo == '':
      MetodosCajero.Volver_a_Caja_principal()
      return
    
    bandera = False
    with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
      for linea in file:
        campos = linea.strip().split(",")
        if articulo.lower() in campos[1].lower() or articulo == campos[0]:
          print()
          articulo = campos[1]
          print(f'Codigo : {campos[0]}')
          print(f'Articulo : {articulo}')
          print(f'Precio : Q {campos[4]}')
          print(f'Stock : {campos[3]} Unidades')
          precio = float(campos[4])
          bandera = True
          break

    if not bandera or articulo == '':
      input('► No se encontró el artículo. Presiona [Enter] para volver a intentar.')
      MetodosCajero.Volver_a_Caja()
      return
    
    cantidad = input('Cantidad de productos (o n para salir) : ')
    if cantidad == 'n' or cantidad == '':
      MetodosCajero.Volver_a_Caja_principal()
    
    subtotal = int(cantidad) * precio
    
    print()
    # Generar voucher
    MetodosCajero.Generar_voucher(articulo, cantidad, precio, subtotal)
    # Actualiza el stock
    MetodosCajero.Actualizar_Stock(articulo, int(cantidad))
    print('\nFacturado correctamente')
    input('Presiona [Enter] para continuar...')
    MetodosCajero.Volver_a_Caja()


  def Consultar_categoria_producto() :

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
      if categoria_producto.lower() == 'n' or categoria_producto == '':
        MetodosCajero.Volver_a_Caja_principal()
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
        print('► No encontrado.')

      # Ingresar la serie
      serie_producto = input('\n> Ingrese la serie (o n para salir) : ') # PREGUNTAR LA SERIE
      if serie_producto.lower() == 'n' or serie_producto == '':
        MetodosCajero.Volver_a_Caja_principal()
        break

      # Imprimir los productos que coinciden con la categoria y serie
      bandera = False
      with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
        print('\nCODIGO \t\tARTICULO \t\t\t\tSTOCK \t\t\tPRECIO')
        for linea in file:
          campos = linea.strip().split(",")
          if serie_producto == campos[2] :
            print(f'{campos[0]} \t\t{campos[1]} \t\t\t{campos[3]} Q \t\t\t{campos[4]}')
            bandera = True

      if not bandera:
        print('► No encontrado.')
      
      print()
      pregunta = input('¿Desea realizar otra consulta? (si/no): ').strip().lower()
      if pregunta == 'si':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
      elif pregunta == 'no' or pregunta == '' or pregunta.isdigit() :
        MetodosCajero.Volver_a_Caja_principal()
        break
      else:
        MetodosCajero.Consultar_categoria()


  def Consultar_codigo_producto():
      while True:
        print('\n\t----- Consulta por codigo del Producto -----')
        id_producto = input('\nIngrese el ID del producto (o n para salir) : ')
        
        if id_producto.lower() == 'n' or id_producto == '' :
          MetodosCajero.Volver_a_Caja_principal()
          break
        
        bandera = False
        with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
            for linea in file:
                campos = linea.strip().split(",")
                if id_producto == campos[0]:
                    print('\t► Encontrado...')
                    print(f'Codigo : {campos[0]}')
                    print(f'Articulo : {campos[1]}')
                    print(f'Precio : Q {campos[4]}')
                    print(f'Stock : {campos[3]}')
                    bandera = True
        if not bandera:
          input('► No encontrado presione [Enter] para continuar...')
          MetodosCajero.Volver_a_Caja_principal()


  def Consultar_descripcion_producto():
    while True:
      print('\n\t----- Consulta por descripcion del Producto -----')
      descripcion_producto = input('\nIngrese la descripcion del producto (o n para salir) : ')

      if descripcion_producto.lower() == 'n':
        MetodosCajero.Volver_a_Caja()
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
        print('► No encontrado.')
        MetodosCajero.Volver_a_Caja()


  def Historial_de_ventas():
    print('\n\t----- Historial de Ventas -----\n')
    with open('Recepcion/Ventas/historial.txt', 'r', encoding='utf-8', errors='ignore') as file:
      for linea in file:
        print(linea.strip())
    print()    


  def Volver_a_Caja() :
    MetodosCajero.Limpiar()
    MetodosCajero.Vender()


  def Volver_a_Caja_principal() :
    MetodosCajero.Limpiar()
    Caja_principal()


  def fecha_actual():
      return datetime.now().strftime("%d/%m/%Y")


  def Limpiar() :
    os.system('cls' if os.name == 'nt' else 'clear')


  def Generar_voucher(articulo, cantidad, precio, subtotal) :
    # Ticket de Venta
    # Fecha: 25/08/2025
    # --------------------------
    # Producto     Cantidad   Precio   Subtotal
    # Pan          2          10.00    20.00
    # Leche        1          15.00    15.00
    # --------------------------
    # TOTAL: 35.00
    print('------- VOUCHER -------')
    print('Articulo : ', articulo)
    print('Cantidad : ', cantidad)
    print('Precio : Q', precio)
    print('Total : Q ', subtotal)


  def Cancelar_venta() :
    pass

  def Salir_sistema():
    sys.exit()


def Caja_principal() :
    
    while True:
      print('\n\t----- Menu Principal -----\n')
      print('1. Vender')
      print('2. Cancelar Venta')
      print('3. Consultar Codigo de Productos')
      print('4. Consultar Descripcion de Producto')
      print('5. Consultar Categoria de Producto')
      print('6. Historial de Ventas')
      print('7. Salir')

      opcion = input('Seleccione una opcion: ')
      match opcion:
        case '1':
          MetodosCajero.Vender()
        case '2':
          MetodosCajero.Cancelar_venta()
        case '3':
          MetodosCajero.Consultar_codigo_producto()
        case '4':
          MetodosCajero.Consultar_descripcion_producto()
        case '5':
          MetodosCajero.Consultar_categoria_producto()
        case '6':
          MetodosCajero.Historial_de_ventas()
        case '7':
          print('Saliendo...')
          sys.exit()
        case _:
          print('Opcion no valida.')


numero_caja = 'Caja 1'
Caja_principal()
