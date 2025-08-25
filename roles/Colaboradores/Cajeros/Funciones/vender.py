print('------- CAJA -------')

print('Ingrese el nombre del producto: ')
nombre_producto = input()
print('Ingrese la cantidad:')
cantidad = int(input())
print('Ingrese el precio:')
precio = float(input())
subtotal = cantidad * precio
print('------- VOUCHER -------')
print('Producto:', nombre_producto)
print('Cantidad:', cantidad)
print('Precio:', precio)
print('Subtotal:', subtotal)