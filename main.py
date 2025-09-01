print('\n\t------ BIENVENIDO ------\n')
print('Seleccione su perfil:')
print('1. Administrador')
print('2. Colaborador')
print('3. Cliente')

match input('→ Ingrese una opcion: '):
    case '1':
        print('Has seleccionado el perfil de Administrador.')
    case '2':
        print('Has seleccionado el perfil de Colaborador.')
    case '3':
        print('Has seleccionado el perfil de Cliente.')
    case _:
        print('Opción no válida.')