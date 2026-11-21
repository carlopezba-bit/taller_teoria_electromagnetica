
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# PROBLEMA 2: CORRIENTES LIBRES DE FRONTERA
# ==========================================

# 1. CONSTANTES Y DATOS

mu0 = 4 * np.pi * 1e-7
mu1 = 5 * mu0
mu2 = 2 * mu0

# Corriente superficial libre (A/m)
Kf = np.array([0.0, 0.0, 10.0])

# Campo magnético del medio 1 (mT)
B1 = np.array([15.0, 20.0, -10.0])

# 2. CÁLCULO DEL CAMPO H1

H1 = (B1 * 1e-3) / mu1

# 3. CONDICIONES DE FRONTERA

# Normal desde el medio 2 hacia el medio 1
n = np.array([0.0, 1.0, 0.0])

# Continuidad normal de B
B2y = B1[1]

# Discontinuidad tangencial de H
H2x = H1[0] + Kf[2]
H2y = (B2y * 1e-3) / mu2
H2z = H1[2]

H2 = np.array([H2x, H2y, H2z])

# Campo B2 (mT)
B2 = mu2 * H2 * 1000

# 4. VERIFICACIÓN

print("RESULTADOS PROBLEMA 2")
print("----------------------")

print("B1 (mT):", np.round(B1, 5))
print("B2 (mT):", np.round(B2, 5))

print("H1 (A/m):", np.round(H1, 2))
print("H2 (A/m):", np.round(H2, 2))

# Comprobación de la condición tangencial
K_calculada = np.cross(n, H1 - H2)

print("Corriente superficial (A/m):",
      np.round(K_calculada, 2))

# 5. SIMULACIÓN GRÁFICA

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Dos proyecciones: x-y y z-y
proyecciones = [
    (0, "Proyección en el plano XY",
     "Coordenada x (m)"),
    (2, "Proyección en el plano ZY",
     "Coordenada z (m)")
]

y_inferior = np.linspace(-3, 0, 100)
y_superior = np.linspace(0, 3, 100)

for ax, titulo_dato in zip(axs, proyecciones):

    componente, titulo, etiqueta = titulo_dato

    # Regiones magnéticas
    ax.axhspan(
        0, 3, color="lightblue", alpha=0.5
    )
    ax.axhspan(
        -3, 0, color="moccasin", alpha=0.6
    )

    # Frontera
    ax.axhline(
        0, color="black", linewidth=2
    )

    # Pendientes de las líneas
    pendiente1 = B1[componente] / B1[1]
    pendiente2 = B2[componente] / B2[1]

    # Distintos puntos de cruce
    for t0 in np.linspace(-3.5, 3.5, 8):

        t_inferior = t0 + pendiente2 * y_inferior
        t_superior = t0 + pendiente1 * y_superior

        # Líneas del medio 2
        ax.plot(
            t_inferior, y_inferior,
            color="darkorange", linewidth=1.8
        )

        # Líneas del medio 1
        ax.plot(
            t_superior, y_superior,
            color="royalblue", linewidth=1.8
        )

        # Flechas de dirección
        for y0, y1, pendiente, color in [
            (-1.9, -1.2, pendiente2, "darkorange"),
            (1.0, 1.7, pendiente1, "royalblue")
        ]:

            ax.annotate(
                "",
                xy=(t0 + pendiente * y1, y1),
                xytext=(t0 + pendiente * y0, y0),
                arrowprops=dict(
                    arrowstyle="->",
                    lw=1.8,
                    color=color
                )
            )

    ax.set_title(titulo)
    ax.set_xlabel(etiqueta)
    ax.set_ylabel("Coordenada normal y (m)")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)

    ax.text(
        -5.7, 2.55,
        "Medio 1: mu_r = 5",
        fontsize=10
    )

    ax.text(
        -5.7, -2.65,
        "Medio 2: mu_r = 2",
        fontsize=10
    )

fig.suptitle(
    "Problema 2: Líneas del campo magnético",
    fontsize=15
)

plt.tight_layout()

# Guardar la figura
Path("graficas").mkdir(exist_ok=True)

plt.savefig(
    "graficas/campo_magnetico.png",
    dpi=300
)

plt.show()
