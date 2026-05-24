import math
import matplotlib.pyplot as plt

def metodo_lugones_plot(P, C=0):

    x_min = math.isqrt(4*P)
    if x_min*x_min < 4*P:
        x_min += 1

    r_min = -x_min
    r_max = -3

    rs = []
    xs = []

    hits_r = []
    hits_x = []

    total_r = 0
    divisiones_exactas = 0
    cuadrados_perfectos = 0

    for r in range(r_min, r_max + 1):

        total_r += 1

        q = r - C

        if q == 0:
            continue

        numerador = -4*P - q*q
        denominador = 2*q

        # curva continua
        x = numerador / denominador

        rs.append(r)
        xs.append(x)

        # ----------------------------------------------------
        # verifica si x da entero exacto
        # ----------------------------------------------------
        if numerador % denominador == 0:

            divisiones_exactas += 1

            xi = numerador // denominador

            n = xi*xi - 4*P

            y = math.isqrt(n)

            # ------------------------------------------------
            # verifica si además da cuadrado perfecto
            # ------------------------------------------------
            if y*y == n:

                cuadrados_perfectos += 1

                hits_r.append(r)
                hits_x.append(xi)

    # ========================================================
    # ESTADÍSTICAS
    # ========================================================

    print("\nESTADÍSTICAS MÉTODO LUGONES")
    print("-" * 50)

    print(f"P = {P}")
    print(f"C = {C}")

    print()

    print(f"r mínimos = {r_min}")
    print(f"r máximos = {r_max}")

    print()

    print(f"Total r revisados = {total_r}")

    print()

    print(f"x enteros exactos = {divisiones_exactas}")

    print(
        f"Porcentaje enteros = "
        f"{100 * divisiones_exactas / total_r:.4f}%"
    )

    print()

    print(f"Cuadrados perfectos = {cuadrados_perfectos}")

    print(
        f"Porcentaje cuadrados perfectos = "
        f"{100 * cuadrados_perfectos / total_r:.6f}%"
    )

    if divisiones_exactas > 0:
        print(
            f"Porcentaje cuadrados dentro de enteros = "
            f"{100 * cuadrados_perfectos / divisiones_exactas:.4f}%"
        )

    # ========================================================
    # PLOT
    # ========================================================

    plt.figure(figsize=(12, 6))

    # curva continua
    plt.plot(rs, xs)

    # hits
    if hits_r:
        plt.scatter(
            hits_r,
            hits_x,
            s=100,
            marker="x"
        )

    plt.xlabel("r")
    plt.ylabel("x")
    plt.title(f"Método Lugones - Curva para P={P}")

    plt.grid(True)
    plt.show()


# ============================================================
# PRUEBA
# ============================================================

P = int("18")

metodo_lugones_plot(P)
