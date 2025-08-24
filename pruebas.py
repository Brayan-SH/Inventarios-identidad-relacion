def producto():
  open("productos.txt", "w")
  productos = [
      {"id": 1, "nombre": "Producto 1", "precio": 10.0},
      {"id": 2, "nombre": "Producto 2", "precio": 20.0},
      {"id": 3, "nombre": "Producto 3", "precio": 30.0}
  ]

  
  for producto in productos:
      line = f"{producto['id']},{producto['nombre']},{producto['precio']}\n"
      open("productos.txt", "a").writelines(line)


  productos[2] = {
    "id": 10,
    "nombre": "Producto 10",
    "precio": 100.0
  }
  
  with open("productos.txt", "a") as file:
    for producto in productos:
        line = f"{producto['id']},{producto['nombre']},{producto['precio']}\n"
        file.write(line)

  with open("productos.txt", "r") as file:
      print(file.read())

producto()

  # print(open("productos.txt").read())

  