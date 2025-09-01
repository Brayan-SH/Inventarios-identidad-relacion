from datetime import datetime 
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
# from Datos.Facturas.Descuentos import descuentos

class MetodosCajero :
  
  def Vender() :

    MetodosCajero.Limpiar()
    print(f'------- VENDER  -------')

    print()
    articulo = input('→ INGRESE LA [descripcion] O [codigo] DEL ARTICULO (o n para salir) : ')
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
          tipo_precio, precio = MetodosCajero.Verificar_precio(precio, campos) # Verifica y muestra precio (normal, oferta, liquidacion)
          
          stocks = campos[3]
          print(f'Stock : {stocks} Unidades')
          
          bandera = True
          break

    # Si no encontró el artículo
    if not bandera or articulo == '' :
      input('>>>>> No se encontró el artículo. Presiona [Enter] para volver a intentar. <<<<<')
      MetodosCajero.Volver_a_Caja()
      return
    
    # Preguntar por descuento de [Averiado / Dañado]
    # O por Cotizacion
    print()
    precio = MetodosCajero.Descuento_manual(precio)    

    print()
    cantidad = input('→ CANTIDAD DE PRODUCTOS (o n para salir) : ')
    cantidad = MetodosCajero.Verificar_cantidad(cantidad)
    
    # Cantidad verificada
    if int(cantidad) > 0 :
      
      # Verificar stocks
      if int(cantidad) > int(stocks) :
        print(f'>>>>> Stock insuficiente. Solo quedan {stocks} unidades. <<<<<')
        input('Presiona [Enter] para continuar...')
        MetodosCajero.Volver_a_Caja()
        return
      
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
          nit = input('2. NOMBRE DEL CLIENTE : ')
        case '3' :
          nit = 'C/F'
          
      descuento = False if tipo_precio in ['precio de oferta', 'precio de liquidacion'] else True

      # Se le puede dar descuento
      if descuento :
        precio_con_descuento, nombre, precio = MetodosCajero.Generar_descuento(nit, precio)
        print(f'Cliente : {nombre}')
      
      else :
        nombre = MetodosCajero.Buscar_colaborador_o_empleado(nit)
        precio_con_descuento = precio_con_descuento if descuento else precio
      
      # Generar factura
      factura = {
        'numero_factura' : MetodosCajero.Generar_numero_factura(),
        'caja' : numero_caja,
        'subtotal' : subtotal,
        'descuentos' : descuento,
        'total' : subtotal - (subtotal * descuento) if descuento else subtotal,
        'forma_pago' : 'Efectivo',
        'estado' : 'Activo',
        'fecha_venta' : MetodosCajero.fecha_actual(),
        'hora_venta' : MetodosCajero.hora_actual(),
      }
      cliente = {
        'nit' : nit,
        'nombre' : nombre,
      }
      productos = {
        'id' : idProducto,
        'articulo' : articulo,
        'cantidad' : cantidad,
        'precio' : precio_con_descuento,
      }
      
      print()
      MetodosCajero.Facturar(factura, cliente, productos)
      
      # Actualiza el stock
      MetodosCajero.Actualizar_stock(articulo, int(cantidad))
      
      # Generar voucher
      subtotal = int(cantidad) * precio_con_descuento if descuento else subtotal
      MetodosCajero.Generar_voucher(articulo, cantidad, precio_con_descuento, subtotal, tipo_precio)

      input('Presiona [Enter] para continuar...')
      
      # Retornar a la caja
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

      categoria_producto = input('\n→ Ingrese la categoria (o n para salir) : ') # PREGUNTAR LA CATEGORIA
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
      serie_producto = input('\n→ Ingrese la serie (o n para salir) : ') # PREGUNTAR LA SERIE
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
                    input('Presione [Enter] para continuar...')
                    MetodosCajero.Volver_a_Caja()
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
            nombre = campos_colaborador[1]
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
            nombre = campos_clientes_frecuentes[2]
            with open('Datos/Facturas/Descuentos/descuentos.txt', 'r', encoding='utf-8', errors='ignore') as file_descuentos:
              for linea_descuento in file_descuentos:
                campos_descuentos = linea_descuento.strip().split(",")
                if campos_clientes_frecuentes[8] == campos_descuentos[0] :
                  precio_con_descuento = precio - (precio * float(campos_descuentos[2]) / 100)
                  bandera = True

    if bandera == False :
      nombre = nit
      precio_con_descuento = precio
      return precio_con_descuento, nombre, precio
    
    return precio_con_descuento, nombre, precio


  def fecha_actual():
      # 14:23:45
      return datetime.now().strftime("%d/%m/%Y").strip()


  def hora_actual():
    """Devuelve la hora actual en formato HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")


  def Limpiar() :
    os.system('cls' if os.name == 'nt' else 'clear')


  def Generar_voucher(articulo, cantidad, precio, subtotal, tipo_precio) :
    # Ticket de Venta
    # Fecha: 25/08/2025
    # --------------------------
    # Producto     Cantidad   Precio   Subtotal
    # Pan          2          10.00    20.00
    # Leche        1          15.00    15.00
    # --------------------------
    # TOTAL: 35.00
    print('Facturado correctamente...\n')
    print('------- VOUCHER -------')
    print('Articulo : ', articulo)
    print('Cantidad : ', cantidad)
    print(f'►{tipo_precio.upper()} : Q {precio}')
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


  def Facturar(factura, cliente, productos) :
    
    with open('Datos/Facturas/facturas_de_ventas.txt', 'a', encoding='utf-8', errors='ignore') as file:
      file.write(f"{factura['numero_factura']},{factura['caja']},{cliente['nit']},{cliente['nombre']},{productos['id']},{productos['articulo']},{productos['cantidad']},{productos['precio']},{factura['subtotal']},{factura['descuentos']},{factura['total']},{factura['forma_pago']},{factura['estado']},{factura['fecha_venta']},{factura['hora_venta']}\n")


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
    return tipo_precio, precio


  def Buscar_colaborador_o_empleado (nit) :
      
      # Si encuentra el nit de [colaborador] descuento
      bandera = False
      with open('Datos/Colaboradores/colaboradores.txt', 'r', encoding='utf-8', errors='ignore') as file_colaborador:
        for linea_colaborador in file_colaborador:
            campos_colaborador = linea_colaborador.strip().split(",")
            if nit == campos_colaborador[7] : # Preguntar por el nit de colaborador
              nombre = campos_colaborador[1]
              bandera = True

      # Si no se encuentra el nit de colaborador que busque en clientes frecuentes
      if bandera == False :
        with open('Datos/Clientes_frecuentes/clientes_frecuentes.txt', 'r', encoding='utf-8', errors='ignore') as file_clientes_frecuentes:
          for linea_clientes_frecuentes in file_clientes_frecuentes :
            campos_clientes_frecuentes = linea_clientes_frecuentes.strip().split(",")
            if nit == campos_clientes_frecuentes[1] : # Preguntar por el nit de cliente frecuente
              nombre = campos_clientes_frecuentes[2]
              bandera = True

      if bandera == False :
        return nit
      
      return nombre


  def Salir_sistema():
    sys.exit()


  def Descuento_manual(precio):
    print('► AGREGAR DESCUENTO MANUALMENTE :')
    print('1. Averiado / Dañado')
    print('2. Cotizacion')
    print('0. Ninguno')
    tipo_descuento = input('→ Opcion : ')
    match tipo_descuento:
        case '1':
            porcentaje_descuento_manual = float(input('→ Ingrese el (0% a 100%) de descuento : '))
            if 0 <= porcentaje_descuento_manual <= 100:
                precio = precio - (precio * porcentaje_descuento_manual / 100)
                print(f'\U0001F449 NUEVO PRECIO CON DESCUENTO DE Q {porcentaje_descuento_manual}% : Q {precio}')
            else:
                print('>>>>> Porcentaje inválido. <<<<<')
                input('Presiona [Enter] para continuar...')
                MetodosCajero.Volver_a_Caja()
                return None
        case '2':
            cotizacion = float(input('→ INGRESE EL PRECIO COTIZADO : Q '))
            if cotizacion > 0 and cotizacion < precio:
                precio = cotizacion
                print(f'\U0001F449 NUEVO PRECIO COTIZADO : Q {precio}')
            else:
                print('>>>>> Precio inválido. <<<<<')
                input('Presiona [Enter] para continuar...')
                MetodosCajero.Volver_a_Caja()
                return None
        case '0' | '':
            pass
        case _:
            print('>>>>> Opción inválida. <<<<<')
            input('Presiona [Enter] para continuar...')
            MetodosCajero.Volver_a_Caja()
            return None
    return precio


  def Verificar_cantidad(cantidad):
    if not cantidad.isdigit():
        print('>>>>> Cantidad inválida. Debe ser un número entero. <<<<<')
        MetodosCajero.Limpiar()
        MetodosCajero.Volver_a_Caja()
        return None
    if cantidad == 'n' or cantidad == '':
        MetodosCajero.Limpiar()
        MetodosCajero.Volver_a_Caja_principal()
        return None
    return int(cantidad)

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