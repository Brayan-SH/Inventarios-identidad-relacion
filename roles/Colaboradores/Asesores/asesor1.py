import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Funciones.funciones as funciones

def Menu_Asesor():
  print('\n\t----- Perfil Asesor -----')
  print('1. Consultar por Codigo')
  print('2. Consultar por Descripcion')
  print('3. Consultar por Categoria')
  print('4. Consultar Stocks bajos')
  print('5. Salir')
  opcion = input('→ Seleccione una opcion : ')

  match opcion:
    case '1':
      funciones.consultar_codigo_producto.consultar_codigo()
    case '2':
      funciones.consultar_descripcion_producto.consultar_descripcion()
    case '3':
      funciones.consultar_por_categoria.consultar_categoria()
    case '4':
      funciones.consultar_stocks_bajos.consultar_stocks()
    case '5':
      print('Saliendo...')
    case _:
      os.system('cls' if os.name == 'nt' else 'clear')
      Menu_Asesor()


Menu_Asesor()