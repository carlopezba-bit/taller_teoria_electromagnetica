
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# PARÁMETROS ORIGINALES
epsilon0 = 8.854e-12
er1 = 4.0
er2 = 2.0
E1 = np.array([6.0, -4.0, 8.0])  # kV/m
sigma_original = 4 * epsilon0 * 1000  # C/m²

Et = np.linalg.norm(E1[:2])

# Función de cálculo
def calcular_campo(er2_valor, sigma_valor):
    E2n = (
        er1 * E1[2] - sigma_valor / (epsilon0 * 1000)
    ) / er2_valor

    theta = np.degrees(np.arctan2(Et, E2n))
    return E2n, theta


# ANÁLISIS 1: CAMBIAR PERMITIVIDAD
permitividades = np.linspace(1, 8, 100)

campos_perm = []
angulos_perm = []

for er in permitividades:
    campo, angulo = calcular_campo(er, sigma_original)
    campos_perm.append(campo)
    angulos_perm.append(angulo)


# ANÁLISIS 2: CAMBIAR CARGA SUPERFICIAL
# q representa sigma_f / (1000 * epsilon0)
q = np.linspace(0, 20, 100)
cargas = q * 1000 * epsilon0

campos_carga = []
angulos_carga = []

for sigma in cargas:
    campo, angulo = calcular_campo(er2, sigma)
    campos_carga.append(campo)
    angulos_carga.append(angulo)


# VALORES ORIGINALES PARA COMPARACIÓN
campo_base, angulo_base = calcular_campo(
    er2, sigma_original
)

# CREACIÓN DE LAS GRÁFICAS
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Gráfica 1
axs[0, 0].plot(permitividades, campos_perm, color="blue")
axs[0, 0].scatter([er2], [campo_base], color="red", zorder=5)
axs[0, 0].set_title("Campo normal vs permitividad")
axs[0, 0].set_xlabel("Permitividad relativa del medio 2")
axs[0, 0].set_ylabel("E2 normal (kV/m)")
axs[0, 0].grid(True)

# Gráfica 2
axs[0, 1].plot(permitividades, angulos_perm, color="green")
axs[0, 1].scatter([er2], [angulo_base], color="red", zorder=5)
axs[0, 1].set_title("Ángulo vs permitividad")
axs[0, 1].set_xlabel("Permitividad relativa del medio 2")
axs[0, 1].set_ylabel("Ángulo theta2 (grados)")
axs[0, 1].grid(True)

# Gráfica 3
axs[1, 0].plot(q, campos_carga, color="purple")
axs[1, 0].scatter([4], [campo_base], color="red", zorder=5)
axs[1, 0].set_title("Campo normal vs carga superficial")
axs[1, 0].set_xlabel("Carga / (1000 * epsilon0)")
axs[1, 0].set_ylabel("E2 normal (kV/m)")
axs[1, 0].grid(True)

# Gráfica 4
axs[1, 1].plot(q, angulos_carga, color="darkorange")
axs[1, 1].scatter([4], [angulo_base], color="red", zorder=5)
axs[1, 1].set_title("Ángulo vs carga superficial")
axs[1, 1].set_xlabel("Carga / (1000 * epsilon0)")
axs[1, 1].set_ylabel("Ángulo theta2 (grados)")
axs[1, 1].grid(True)

fig.suptitle(
    "Problema 1 - Análisis de sensibilidad",
    fontsize=15
)

plt.tight_layout()

Path("graficas").mkdir(exist_ok=True)
plt.savefig(
    "graficas/sensibilidad_electrica.png",
    dpi=300
)

plt.show()

print("RESULTADOS ORIGINALES")
print(f"E2 normal: {campo_base:.2f} kV/m")
print(f"Ángulo theta2: {angulo_base:.2f} grados")
print("Análisis de sensibilidad finalizado.")
