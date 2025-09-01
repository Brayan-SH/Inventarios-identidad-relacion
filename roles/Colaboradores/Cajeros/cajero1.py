import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from roles.Colaboradores.Cajeros.Funciones import caja

caja.Caja_principal()