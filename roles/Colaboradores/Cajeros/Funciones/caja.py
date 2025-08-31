from datetime import datetime 
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
# from Datos.Facturas.Descuentos import descuentos

class MetodosCajero :
  
  def Vender() :

    MetodosCajero.Limpiar()
    print(f'------- VENDER  -------')

    print()
    articulo = input('INGRESE LA [descripcion] O [codigo] DEL ARTICULO (o n para salir) : ')
    if articulo.lower() == 'n' or articulo == '':
      MetodosCajero.Volver_a_Caja_principal()
      return
    
    bandera = False
    with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
      for linea in file:
        campos = linea.strip().split(",")
        if articulo.lower() in campos[1].lower() or articulo == campos[0]:

          # Mostrar información del producto
          print()
          idProducto = campos[0]
          articulo = campos[1]
          print(f'Codigo : {idProducto}')
          print(f'Articulo : {articulo}')
          
          precio = float(campos[4])
          tipo_precio = MetodosCajero.Verificar_precio(precio, campos) # Verifica y muestra precio (normal, oferta, liquidacion)
          
          stocks = campos[3]
          print(f'Stock : {stocks} Unidades')
          producto = [idProducto, articulo]
          
          bandera = True
          break

    # Si no se encontró el artículo
    if not bandera or articulo == '' :
      input('► No se encontró el artículo. Presiona [Enter] para volver a intentar.')
      MetodosCajero.Volver_a_Caja()
      return
    
    print()
    cantidad = input('CANTIDAD DE PRODUCTOS (o n para salir) : ')

    # Si la cantidad no es un número entero
    if not cantidad.isdigit() :
      print('► Cantidad inválida. Debe ser un número entero.')
      MetodosCajero.Limpiar()
      MetodosCajero.Volver_a_Caja()

    # Si la cantidad es 'n' o vacía
    if cantidad == 'n' or cantidad == '' :
        MetodosCajero.Limpiar()
        MetodosCajero.Volver_a_Caja_principal()

    # Cantidad verificada
    if int(cantidad) > 0 :
      
      # Verificar stocks
      # if stocks > 0 :
      #   pass
      subtotal = int(cantidad) * precio
      print(f'\U0001F4B0 Subtotal : Q {subtotal}')

      print('\n1. NIT DEL CLIENTE')
      print('2. NOMBRE DEL CLIENTE')
      print('3. C/F')
      opcion = input('Opción : ')
      match opcion :
        case '1' :
          nit = input('1. NIT DEL CLIENTE : ')
        case '2' :
          nombre = input('2. NOMBRE DEL CLIENTE : ')
        case '3' :
          cf = 'C/F'
          
      descuento = False if tipo_precio in ['precio de oferta', 'precio de liquidacion'] else True

      if descuento :
        precio_con_descuento = MetodosCajero.Generar_descuento(nit, precio)
      
      elif False :
        # Si no tiene descuento : Buscar el precio o Obtener el precio
        pass

      print()
      producto.extend([cantidad, precio, subtotal])
      # Generar factura
      factura = {
        'numero' : MetodosCajero.Generar_numero_factura(),
        'caja' : numero_caja,
      }
      # MetodosCajero.Facturar(articulo, cantidad, precio, subtotal)
      # Actualiza el stock
      MetodosCajero.Actualizar_stock(articulo, int(cantidad))
      print('\nFacturado correctamente')
      # Generar voucher
      # subtotal = int(cantidad) * precio_con_descuento if descuento else subtotal
      subtotal = int(cantidad) * precio_con_descuento if descuento else subtotal
      MetodosCajero.Generar_voucher(articulo, cantidad, precio_con_descuento, subtotal)
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
    with open('Datos/Facturas/facturas_de_ventas.txt', 'r', encoding='utf-8', errors='ignore') as file:
      for linea in file:
        print(linea.strip())
    print()    


  def Volver_a_Caja() :
    MetodosCajero.Limpiar()
    MetodosCajero.Vender()


  def Volver_a_Caja_principal() :
    MetodosCajero.Limpiar()
    Caja_principal()
    
    
  def Generar_numero_factura():
      """Genera un número de factura único basado en la fecha y hora actual."""
      return datetime.now().strftime("F%Y%m%d%H%M%S")


  def Generar_descuento (nit, precio) :
    
    # Si encuentra el nit de [colaborador] descuento
    bandera = False
    with open('Datos/Colaboradores/colaboradores.txt', 'r', encoding='utf-8', errors='ignore') as file_colaborador:
      for linea_colaborador in file_colaborador:
          campos_colaborador = linea_colaborador.strip().split(",")
          
          if nit == campos_colaborador[7] : # Preguntar por el nit de colaborador
            with open('Datos/Facturas/Descuentos/descuentos.txt', 'r', encoding='utf-8', errors='ignore') as file_descuentos:
              for linea_descuento in file_descuentos:
                  campos_descuentos = linea_descuento.strip().split(",")
                  if campos_colaborador[6] == campos_descuentos[0] : # Si encuentra el codigo de descuento
                    precio_con_descuento = precio - (precio * float(campos_descuentos[2]) / 100)
                    bandera = True

    # Si no se encuentra el nit de colaborador que busque en clientes frecuentes
    if bandera == False :
      with open('Datos/Clientes_frecuentes/clientes_frecuentes.txt', 'r', encoding='utf-8', errors='ignore') as file_clientes_frecuentes:
        for linea_clientes_frecuentes in file_clientes_frecuentes :
          campos_clientes_frecuentes = linea_clientes_frecuentes.strip().split(",")
          if nit == campos_clientes_frecuentes[1] : # Preguntar por el nit de cliente frecuente
            with open('Datos/Facturas/Descuentos/descuentos.txt', 'r', encoding='utf-8', errors='ignore') as file_descuentos:
              for linea_descuento in file_descuentos:
                campos_descuentos = linea_descuento.strip().split(",")
                if campos_clientes_frecuentes[8] == campos_descuentos[0] :
                  precio_con_descuento = precio - (precio * float(campos_descuentos[2]) / 100)
                  bandera = True

    if bandera == False :
      precio_con_descuento = precio
      return precio_con_descuento
    
    return precio_con_descuento

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
    print(f'► Precio con descuento : Q {precio}')
    print('Total : Q ', subtotal)


  def Actualizar_stock(articulo, cantidad):
    productos_path = 'Recepcion/Productos/productos.txt'
    productos_actualizados = []
    actualizado = False

    with open(productos_path, 'r', encoding='utf-8', errors='ignore') as file:
      for linea in file:
        campos = linea.strip().split(",")
        # Busca por código o nombre
        if articulo == campos[0] or articulo.lower() == campos[1].lower() :
          stock_actual = int(campos[3])
          nuevo_stock = max(stock_actual - cantidad, 0) # Asegura que el stock no sea negativo
          campos[3] = str(nuevo_stock)
          actualizado = True
        productos_actualizados.append(",".join(campos))

    if actualizado:
      with open(productos_path, 'w', encoding='utf-8', errors='ignore') as file:
        for linea in productos_actualizados :
          file.write(linea + "\n")
    else:
      print("\n► No se pudo actualizar el stock: producto no encontrado.")


  def Facturar(factura, cliente, productos, pago) :
    
    with open('Datos/Facturas/facturas_de_ventas.txt', 'a', encoding='utf-8', errors='ignore') as file:
        for producto in productos:
            file.write(f"{factura['numero_factura']},{factura['caja']},{cliente['nit']},{cliente['nombre']},{producto['id']},{producto['articulo']},{producto['cantidad']},{producto['precio']},{producto['subtotal']},{producto['descuentos']},{producto['total']},{pago['forma_pago']},{pago['estado']}, {pago['fecha_venta']},{pago['hora_venta']}\n")


  def Determinar_tipo_descuento(codigo_descuento):
      return Descuentos.get(codigo_descuento, {'tipo': 'Sin Descuento', 'porcentaje': 0})


  def Cancelar_venta() :
    pass


  def Verificar_precio(precio, campos) :
    match precio :
      case _ if precio > 0 :
        print(f'Precio : Q {precio} ► PRECIO NORMAL.') # Si es precio normal.
        tipo_precio = 'precio normal'
      case _ if float(campos[5]) > 0 :
        precio = float(campos[5])
        print(f'Precio : Q {precio} ► PRECIO DE OFERTA, SIN DESCUENTO.') # Si es precio de oferta.
        tipo_precio = 'precio de oferta'
      case _ :
        precio = float(campos[6])
        print(f'Precio : Q {precio} ► PRECIO DE LIQUIDACIÓN, SIN DESCUENTO.') # Si es precio de liquidación.
        tipo_precio = 'precio de liquidacion'
    return tipo_precio


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
