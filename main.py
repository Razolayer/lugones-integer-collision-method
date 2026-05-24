import math
import time

def es_cuadrado(n):
    y = math.isqrt(n)
    return y*y == n, y

def metodo_lugones_directo(P, C=0):
    t0 = time.perf_counter()

    x_min = math.isqrt(4*P)
    if x_min*x_min < 4*P:
        x_min += 1

    x_max = P  # evita trivial P+1

    # Para C=0: r = y - x
    # Rango aproximado de r
    y_min = math.isqrt(x_min*x_min - 4*P)
    r_min = y_min - x_min + C
    r_max = -3 + C   # evita trivial r=-2+C

    print("MÉTODO LUGONES DIRECTO")
    print("-" * 50)
    print(f"P = {P}")
    print(f"C = {C}")
    print(f"x_min = {x_min}")
    print(f"x_max = {x_max}")
    print(f"r desde {r_min} hasta {r_max}")
    print("-" * 50)

    revisados = 0

    for r in range(r_min, r_max + 1):
        revisados += 1

        # Ajuste si C no es cero
        q = r - C

        if q == 0:
            continue

        numerador = -4*P - q*q
        denominador = 2*q

        if numerador % denominador != 0:
            continue

        x = numerador // denominador

        if x < x_min or x > x_max:
            continue

        n = x*x - 4*P
        ok, y = es_cuadrado(n)

        if ok:
            valor_exacto = y - x + C

            if valor_exacto == r:
                print("✅ ENTERO ENCONTRADO")
                print("-" * 50)
                print(f"r = {r}")
                print(f"x = {x}")
                print(f"y = {y}")
                print(f"f(x) exacto = {valor_exacto}")
                print(f"enteros revisados = {revisados}")
                print(f"tiempo = {time.perf_counter() - t0:.6f} s")
                return x, y, r

    print("No se encontró entero no trivial.")
    print(f"enteros revisados = {revisados}")
    print(f"Tiempo total = {time.perf_counter() - t0:.6f} s")
    return None


P = int("2000000014")
metodo_lugones_directo(P, C=0)
