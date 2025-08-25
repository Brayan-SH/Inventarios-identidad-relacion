def producto():
  
  productos = [
      {"id": 1, "nombre": "Producto 1", "precio": 10.0},
      {"id": 2, "nombre": "Producto 2", "precio": 20.0},
      {"id": 3, "nombre": "Producto 3", "precio": 30.0}
  ]
  
  # Agrega todos los productos (incluyendo el nuevo) en modo 'w' para limpiar el archivo
  productos.append({
    "id": 10,
    "nombre": "Producto 10",
    "precio": 100.0
  })
  
  with open("productos.txt", "w") as file:
    for producto in productos:
      line = f"{producto['id']},{producto['nombre']},{producto['precio']}\n"
      file.write(line)

  # Lee los productos
  with open("productos.txt", "r") as file:
    row = file.readlines() # Obtiene las lineas en una lista.
    row = [line.strip().split(',') for line in row] # Convierte cada línea en una lista.
    print(row)
    
# producto()
x = '1'
print(x.rjust(2, "0"))
  