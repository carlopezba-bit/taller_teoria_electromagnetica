
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# =========================================
# PROBLEMA 2 - ANÁLISIS DE SENSIBILIDAD
# =========================================

# 1. CONSTANTES Y PARÁMETROS

mu0 = 4 * np.pi * 1e-7

mur1 = 5.0
mur2 = 2.0

# Campo B1 en mT
B1 = np.array([15.0, 20.0, -10.0])

# Corriente superficial libre (A/m)
Kf_original = 10.0

# 2. FUNCIÓN PARA CALCULAR B2

def calcular_campo(mur2_valor, Kf_valor):

    mu1 = mur1 * mu0
    mu2 = mur2_valor * mu0

    # Convertir B1 a teslas
    B1_T = B1 * 1e-3

    H1 = B1_T / mu1

    # Condiciones de frontera
    H2x = H1[0] + Kf_valor
    H2y = B1_T[1] / mu2
    H2z = H1[2]

    H2 = np.array([H2x, H2y, H2z])

    # Campo B2 en mT
    B2 = mu2 * H2 * 1000

    # Magnitud total del campo
    magnitud_B2 = np.linalg.norm(B2)

    # Ángulo respecto a la normal y
    Bt = np.sqrt(B2[0]**2 + B2[2]**2)

    theta2 = np.degrees(
        np.arctan2(Bt, abs(B2[1]))
    )

    return B2, magnitud_B2, theta2


# 3. CONDICIONES ORIGINALES

B2_base, magnitud_base, theta_base = calcular_campo(
    mur2, Kf_original
)

print("RESULTADOS ORIGINALES")
print("---------------------")
print("B2 (mT):", np.round(B2_base, 5))
print(f"Magnitud B2: {magnitud_base:.4f} mT")
print(f"Ángulo theta2: {theta_base:.4f} grados")


# 4. ANÁLISIS DE PERMEABILIDAD

permeabilidades = np.linspace(1, 8, 150)

magnitudes_perm = []
angulos_perm = []

for valor in permeabilidades:

    B2, magnitud, theta = calcular_campo(
        valor, Kf_original
    )

    magnitudes_perm.append(magnitud)
    angulos_perm.append(theta)


# 5. ANÁLISIS DE CORRIENTE SUPERFICIAL

corrientes = np.linspace(0, 3000, 150)

componentes_Bx = []
angulos_corriente = []

for K in corrientes:

    B2, magnitud, theta = calcular_campo(
        mur2, K
    )

    componentes_Bx.append(B2[0])
    angulos_corriente.append(theta)


# 6. CREACIÓN DE GRÁFICAS

fig, axs = plt.subplots(2, 2, figsize=(13, 9))

# Gráfica 1: Magnitud vs permeabilidad

axs[0, 0].plot(
    permeabilidades,
    magnitudes_perm,
    color="blue",
    linewidth=2
)

axs[0, 0].scatter(
    [mur2], [magnitud_base],
    color="red", zorder=5
)

axs[0, 0].set_title(
    "Magnitud de B2 vs permeabilidad"
)

axs[0, 0].set_xlabel(
    "Permeabilidad relativa del medio 2"
)

axs[0, 0].set_ylabel("|B2| (mT)")
axs[0, 0].grid(True)


# Gráfica 2: Ángulo vs permeabilidad

axs[0, 1].plot(
    permeabilidades,
    angulos_perm,
    color="green",
    linewidth=2
)

axs[0, 1].scatter(
    [mur2], [theta_base],
    color="red", zorder=5
)

axs[0, 1].set_title(
    "Ángulo de refracción vs permeabilidad"
)

axs[0, 1].set_xlabel(
    "Permeabilidad relativa del medio 2"
)

axs[0, 1].set_ylabel("Ángulo theta2 (grados)")
axs[0, 1].grid(True)


# Gráfica 3: Componente Bx vs corriente

axs[1, 0].plot(
    corrientes,
    componentes_Bx,
    color="purple",
    linewidth=2
)

axs[1, 0].scatter(
    [Kf_original], [B2_base[0]],
    color="red", zorder=5
)

axs[1, 0].set_title(
    "Componente B2x vs corriente superficial"
)

axs[1, 0].set_xlabel(
    "Corriente superficial Kf (A/m)"
)

axs[1, 0].set_ylabel("B2x (mT)")
axs[1, 0].grid(True)


# Gráfica 4: Ángulo vs corriente

axs[1, 1].plot(
    corrientes,
    angulos_corriente,
    color="darkorange",
    linewidth=2
)

axs[1, 1].scatter(
    [Kf_original], [theta_base],
    color="red", zorder=5
)

axs[1, 1].set_title(
    "Ángulo de refracción vs corriente"
)

axs[1, 1].set_xlabel(
    "Corriente superficial Kf (A/m)"
)

axs[1, 1].set_ylabel(
    "Ángulo theta2 (grados)"
)

axs[1, 1].grid(True)


# 7. GUARDAR RESULTADOS

fig.suptitle(
    "Problema 2 - Análisis de sensibilidad magnética",
    fontsize=15
)

plt.tight_layout()

Path("graficas").mkdir(exist_ok=True)

plt.savefig(
    "graficas/sensibilidad_magnetica.png",
    dpi=300
)

plt.show()

print("\nAnálisis de sensibilidad finalizado.")
