class caja :
  def __init__(self, numero_caja, codigo_producto, descripcion_producto) :
    self.numero_caja = numero_caja
    self.codigo_producto = codigo_producto
    self.descripcion_producto = descripcion_producto

  def vender(self) :
    print(f'-------  {self.numero_caja} -------')

    descripcion_producto_or_codigo_producto = input('Ingrese la descripcion o codigo del producto : ')
    cantidad = float(input('Ingrese la cantidad:'))
    precio = 1 # jalar el precio del producto.txt
    subtotal = cantidad * precio
    
    print('------- VOUCHER -------')
    print('Producto:', descripcion_producto_or_codigo_producto)
    print('Cantidad:', cantidad)
    print('Precio:', precio)
    print('Subtotal:', subtotal)
    pass


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
