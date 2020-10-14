from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

def caso_L():
    # Unidades base
    m = 1.
    kg = 1.
    s = 1.

    # Unidades derivadas
    N = kg * m / s**2
    cm = 0.01 * m
    mm = 0.001 * m
    KN = 1000 * N

    Pa = N / m**2
    KPa = 1000 * Pa
    MPa = 1000 * KPa
    GPa = 1000 * MPa

    # Parametros
    L = 5.0 * m
    F = 100 * KN
    B = 2.0 * m


    # Inicializar modelo
    ret = Reticulado()

    # Nodos
    ret.agregar_nodo(0, 0,  0)
    ret.agregar_nodo(L, 0,  0)
    ret.agregar_nodo(2 * L, 0,  0)
    ret.agregar_nodo(L / 2, B / 2, sqrt(3) / 2 * L)
    ret.agregar_nodo(3 * L / 2, B / 2, sqrt(3) / 2 * L)
    ret.agregar_nodo(0, B, 0)
    ret.agregar_nodo(L, B, 0)
    ret.agregar_nodo(2 * L, B, 0)


    # Barras
    A = (1.1 * cm)**2
    r = sqrt(A / 3.141593)
    props = [r, r, 200 * GPa, 7600 * kg / m**3, 420 * MPa]

    props2 = [r, r, 200 * GPa, 7600 * kg / m**3, 420 * MPa]

    # props2 = [0.6*r, 0.6*r, 200*GPa, 7600*kg/m**3, 420*MPa]

    ret.agregar_barra(Barra(0, 1, *props))   # 0
    ret.agregar_barra(Barra(1, 2, *props))   # 1
    ret.agregar_barra(Barra(2, 3, *props))   # 2
    ret.agregar_barra(Barra(0, 3, *props2))   # 3
    ret.agregar_barra(Barra(4, 5, *props2))   # 4
    ret.agregar_barra(Barra(5, 6, *props2))   # 5
    ret.agregar_barra(Barra(7, 8, *props))   # 6
    ret.agregar_barra(Barra(8, 9, *props))   # 7
    ret.agregar_barra(Barra(9, 10, *props))   # 8
    ret.agregar_barra(Barra(0, 7, *props2))   # 9
    ret.agregar_barra(Barra(7, 8, *props2))   # 10
    ret.agregar_barra(Barra(1, 8, *props2))   # 11
    ret.agregar_barra(Barra(0, 8, *props))   # 12
    ret.agregar_barra(Barra(1, 7, *props))   # 13
    ret.agregar_barra(Barra(1, 9, *props))   # 14
    ret.agregar_barra(Barra(2, 8, *props))   # 15
    ret.agregar_barra(Barra(2, 9, *props))   # 16
    ret.agregar_barra(Barra(2, 10, *props))   # 17
    ret.agregar_barra(Barra(3, 9, *props))   # 18
    ret.agregar_barra(Barra(3, 10, *props))   # 19
    ret.agregar_barra(Barra(0, 4, *props))   # 20
    ret.agregar_barra(Barra(1, 4, *props))   # 21
    ret.agregar_barra(Barra(4, 7, *props))   # 19
    ret.agregar_barra(Barra(4, 8, *props))   # 22
    ret.agregar_barra(Barra(5, 8, *props))   # 23
    ret.agregar_barra(Barra(1, 5, *props))   # 24
    ret.agregar_barra(Barra(2, 5, *props))   # 25
    ret.agregar_barra(Barra(5, 9, *props))   # 26
    ret.agregar_barra(Barra(6, 9, *props))   # 27
    ret.agregar_barra(Barra(2, 9, *props))   # 28
    ret.agregar_barra(Barra(6, 10, *props))   # 29
    ret.agregar_barra(Barra(3, 6, *props))   # 30
    
    # ver_reticulado_3d(ret)


    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)

    ret.agregar_restriccion(2, 2, 0)
    ret.agregar_restriccion(5, 2, 0)
    ret.agregar_restriccion(7, 2, 0)

    ret.agregar_restriccion(5, 0, 0)


    # 0-----]-----1-----]-----2-----]-----3
    # |     ]     |     ]     |     ]     |
    # |-----]-----|-----]-----|-----]-----|
    # |     ]     |     ]     |     ]     |
    # 7-----]-----8-----]-----9-----]-----10

    # A0265 sera el area entre 0,1,8,7
    # A1276 sera el area entre 1,2,9,8
    # A23109 sera el area entre 2,3,10,9

    q = 400  # kg/m2
    barras = ret.obtener_barras()

    L_01 = barras[0].calcular_largo(ret)
    L_07 = barras[16].calcular_largo(ret)
    A0187 = L_01 * L_07  # m2

    L_12 = barras[1].calcular_largo(ret)
    L_18 = barras[15].calcular_largo(ret)
    A1298 = L_12 * L_18  # m2
    
    L_23 = barras[2].calcular_largo(ret)
    L_29 = barras[19].calcular_largo(ret)
    A23109 = L_23 * L_29  # m2

    [ret.agregar_fuerza(i, 2, -A0187 * q / 4) for i in [0, 1, 8, 7]]
    [ret.agregar_fuerza(i, 2, -A1298 * q / 4) for i in [1, 2, 9, 8]]
    [ret.agregar_fuerza(i, 2, -A23109 * q / 4) for i in [2, 3, 10, 9]]

    return ret





# peso = ret.calcular_peso_total()

# print(f"peso = {peso}")


# ret.ensamblar_sistema()
# ret.resolver_sistema()
# f = ret.recuperar_fuerzas()
# fu = ret.recuperar_factores_de_utilizacion(f)


# ver_reticulado_3d(ret,
#                   opciones_nodos={
#                       "usar_posicion_deformada": True,
#                       "factor_amplificacion_deformada": 30.,
#                   },
#                   opciones_barras={
#                       "color_barras_por_dato": True,
#                       "ver_numeros_de_barras": False,
#                       "ver_dato_en_barras": True,
#                       "dato": fu,
#                       "color_fondo": [1, 1, 1, 0.4]
#                   })

# barras_a_rediseñar = [3, 4, 5, 9, 10, 11]
# barras = ret.obtener_barras()
# for i in barras_a_rediseñar:
#     barras[i].rediseñar(f[i])


# ret.ensamblar_sistema()
# ret.resolver_sistema()
# f1 = ret.recuperar_fuerzas()
# fu1 = ret.recuperar_factores_de_utilizacion(f)

# peso = ret.calcular_peso_total()

# print(f"peso = {peso}")

# ver_reticulado_3d(ret,
#                   opciones_nodos={
#                       "usar_posicion_deformada": True,
#                       "factor_amplificacion_deformada": 30.,
#                   },
#                   opciones_barras={
#                       "color_barras_por_dato": True,
#                       "ver_numeros_de_barras": False,
#                       "ver_dato_en_barras": True,
#                       "dato": fu1,
#                       "color_fondo": [1, 1, 1, 0.4]
