class Caja :
  
  def Vender(self, numero_caja) :
    self.numero_caja = numero_caja
    print(f'-------  {self.numero_caja} -------')

    articulo = input('Ingrese la descripcion o codigo del articulo : ')
    bandera = False
    with open('Recepcion/Productos/productos.txt', 'r', encoding='utf-8', errors='ignore') as file:
      for linea in file:
        campos = linea.strip().split(",")
        if articulo.lower() in campos[1].lower() or articulo == campos[0]:
          print()
          articulo = campos[1]
          print(f'Codigo : {campos[0]}')
          print(f'Articulo : {campos[1]}')
          print(f'Precio : Q {campos[4]}')
          print(f'Stock : {campos[3]} Unidades')
          precio = float(campos[4])
          bandera = True
          break

    if not bandera:
      self.Vender(numero_caja)
      return

    cantidad = int(input('Cantidad de productos : '))
    subtotal = cantidad * precio
    
    print()
    print('------- VOUCHER -------')
    print('Articulo : Q', articulo)
    print('Cantidad : ', cantidad)
    print('Precio : Q', precio)
    print('Total : Q ', subtotal)

caja1 = Caja()
caja1.Vender('Caja 1')

class cancelar_venta :
  pass


class consultar_codigo_productos :
  pass


class consultar_descripcion_producto :
  pass


class generar_voucher :
  # Ticket de Venta
  # Fecha: 25/08/2025
  # --------------------------
  # Producto     Cantidad   Precio   Subtotal
  # Pan          2          10.00    20.00
  # Leche        1          15.00    15.00
  # --------------------------
  # TOTAL: 35.00
  pass


class historial_ventas :
  pass


class consultar_stocks_bajos :
  pass
