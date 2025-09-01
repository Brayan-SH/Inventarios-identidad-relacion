import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from roles.Colaboradores.Cajeros.Funciones import caja

numero_caja = 'Caja 1'
caja.Caja_principal()