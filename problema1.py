
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# DATOS DEL PROBLEMA
epsilon0 = 8.854e-12
epsilon1 = 4 * epsilon0
epsilon2 = 2 * epsilon0
sigma_f = 4 * epsilon0 * 1000

# Campo eléctrico del medio 1 (kV/m)
E1 = np.array([6.0, -4.0, 8.0])

# CONDICIONES DE FRONTERA
# Las componentes tangenciales se conservan
E2x = E1[0]
E2y = E1[1]

# Discontinuidad del desplazamiento normal
E2z = (epsilon1 * E1[2] * 1000 - sigma_f) / (
    epsilon2 * 1000
)

E2 = np.array([E2x, E2y, E2z])

# Magnitud tangencial
Et = np.linalg.norm(E1[:2])

# Ángulos con la normal
theta1 = np.degrees(np.arctan2(Et, E1[2]))
theta2 = np.degrees(np.arctan2(Et, E2[2]))

print("Campo E1:", E1, "kV/m")
print("Campo E2:", E2, "kV/m")
print(f"Ángulo medio 1: {theta1:.2f} grados")
print(f"Ángulo medio 2: {theta2:.2f} grados")

# SIMULACIÓN DE LAS LÍNEAS DE CAMPO
fig, ax = plt.subplots(figsize=(10, 7))

# Regiones dieléctricas
ax.axhspan(0, 3, color="lightblue", alpha=0.45)
ax.axhspan(-3, 0, color="moccasin", alpha=0.55)

# Frontera z = 0
ax.axhline(0, color="black", linewidth=2)

z_abajo = np.linspace(-3, 0, 100)
z_arriba = np.linspace(0, 3, 100)

# Los puntos de cruce son distintos para cada línea
for t0 in np.linspace(-4, 4, 9):

    # Pendiente de cada línea respecto a z
    t_abajo = t0 + (Et / E2[2]) * z_abajo
    t_arriba = t0 + (Et / E1[2]) * z_arriba

    ax.plot(t_abajo, z_abajo, color="darkorange", lw=1.8)
    ax.plot(t_arriba, z_arriba, color="royalblue", lw=1.8)

    # Flechas en el sentido del campo
    for z0, z1, En, color in [
        (-1.8, -1.1, E2[2], "darkorange"),
        (1.0, 1.7, E1[2], "royalblue")
    ]:
        ax.annotate(
            "",
            xy=(t0 + Et / En * z1, z1),
            xytext=(t0 + Et / En * z0, z0),
            arrowprops=dict(
                arrowstyle="->",
                color=color,
                lw=1.8
            )
        )

ax.text(-6.5, 2.5, "Medio 1: epsilon_r = 4", fontsize=11)
ax.text(-6.5, -2.6, "Medio 2: epsilon_r = 2", fontsize=11)
ax.text(4.2, 0.15, "Frontera z = 0", fontsize=10)

ax.set_xlim(-7, 7)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.set_xlabel("Coordenada tangencial t (m)")
ax.set_ylabel("Coordenada normal z (m)")
ax.set_title("Problema 1: Líneas del campo eléctrico")
ax.grid(alpha=0.2)

plt.tight_layout()

# Guardar la gráfica para el informe
Path("graficas").mkdir(exist_ok=True)
plt.savefig("graficas/campo_electrico.png", dpi=300)

plt.show()
