# Taller de Teoría Electromagnética

### Condiciones de frontera en interfaces dieléctricas y magnéticas: refracción de campos y fuentes ligadas

**Universidad Nacional de Colombia**  
**Facultad de Minas — Sede Medellín**  
**Asignatura:** Teoría Electromagnética  
**Docente:** Gustavo Gutiérrez Rodríguez  
**Tipo de actividad:** Taller grupal — Simulaciones computacionales

---

## Integrantes

| Estudiante | Institución |
|---|---|
| Carlos José López Bacca | Universidad Nacional de Colombia |
| Juan José Cadavid Torres | Universidad Nacional de Colombia |
| Esteban Ossa Lopera | Universidad Nacional de Colombia |

---

## Descripción del proyecto

Este repositorio contiene el desarrollo computacional del taller de **Teoría Electromagnética**, enfocado en el estudio de las condiciones de frontera entre medios dieléctricos y magnéticos lineales, homogéneos e isotrópicos.

El trabajo comprende la solución analítica de dos problemas, complementada mediante simulaciones desarrolladas en Python para representar el comportamiento de los campos electromagnéticos en las interfaces y realizar análisis de sensibilidad respecto a los parámetros físicos involucrados.

Las simulaciones permiten comprobar los resultados matemáticos, visualizar la refracción de los campos y analizar la influencia de las propiedades electromagnéticas de los materiales.

## Objetivo general

Analizar y verificar las condiciones de frontera electromagnéticas entre dos medios materiales mediante procedimientos matemáticos y simulaciones computacionales desarrolladas en Python.

## Problemas desarrollados

### Problema 1. Interfaces dieléctricas cargadas

Se estudia una interfaz plana entre dos medios dieléctricos con diferentes permitividades relativas y una densidad superficial de carga libre.

**Parámetros iniciales:**

- Permitividad relativa del medio 1: εr₁ = 4
- Permitividad relativa del medio 2: εr₂ = 2
- Densidad superficial de carga libre: σf = 4000ε₀ C/m²
- Frontera: z = 0
- Campo eléctrico inicial: E₁ = (6, −4, 8) kV/m

**Actividades realizadas:**

- Descomposición del campo eléctrico en componentes tangenciales y normales.
- Aplicación de las condiciones de frontera electrostáticas.
- Cálculo de los vectores de desplazamiento y polarización eléctrica.
- Determinación de las densidades superficiales de carga ligada.
- Cálculo de los ángulos de refracción.
- Simulación de las líneas del campo eléctrico.
- Análisis de sensibilidad respecto a la permitividad y la carga superficial libre.

**Resultados principales:**

| Magnitud | Resultado |
|---|---|
| Campo eléctrico E₂ | (6, −4, 14) kV/m |
| Ángulo θ₁ | 42.03° |
| Ángulo θ₂ | 27.25° |

### Problema 2. Corrientes libres de frontera

Se analiza una interfaz plana entre dos medios magnéticos con diferentes permeabilidades relativas y una densidad superficial de corriente libre.

**Parámetros iniciales:**

- Permeabilidad relativa del medio 1: μr₁ = 5
- Permeabilidad relativa del medio 2: μr₂ = 2
- Corriente superficial libre: Kf = 10 A/m en dirección positiva del eje z
- Frontera: y = 0
- Densidad de flujo magnético inicial: B₁ = (15, 20, −10) mT

**Actividades realizadas:**

- Determinación de la intensidad del campo magnético.
- Aplicación de las condiciones de frontera magnetostáticas.
- Cálculo de los vectores de magnetización.
- Determinación de la corriente superficial ligada.
- Verificación de la ley de refracción magnética en ausencia de corriente libre.
- Simulación de las líneas del campo magnético.
- Análisis de sensibilidad respecto a la permeabilidad y la corriente superficial.

**Resultados principales:**

| Magnitud | Resultado |
|---|---|
| Campo magnético H₂ | (2397.32, 7957.75, −1591.55) A/m |
| Densidad de flujo B₂ | (6.02513, 20, −4) mT |
| Ángulo θ₂ con Kf = 10 A/m | 19.88° |
| Ángulo θ₂ con Kf = 0 | 19.83° |

---

## Estructura del repositorio

| Archivo o carpeta | Descripción |
|---|---|
| `problema1.py` | Simulación de las líneas del campo eléctrico en dos medios dieléctricos. |
| `sensibilidad1.py` | Análisis de sensibilidad de la permitividad y la carga superficial libre. |
| `problema2.py` | Simulación de las líneas del campo magnético en dos medios magnéticos. |
| `sensibilidad2.py` | Análisis de sensibilidad de la permeabilidad y la corriente superficial. |
| `gráficos/` | Imágenes de las simulaciones y análisis de sensibilidad realizados. |

## Herramientas y tecnologías

El proyecto fue desarrollado utilizando:

- **Python:** lenguaje de programación empleado para implementar los modelos matemáticos.
- **NumPy:** operaciones vectoriales y cálculos numéricos.
- **Matplotlib:** generación de gráficas y visualización de campos electromagnéticos.
- **Visual Studio Code:** entorno de desarrollo y ejecución.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

## Instalación y ejecución

**1. Clonar el repositorio**

Desde GitHub, copiar la dirección HTTPS del repositorio y ejecutar:

`git clone URL_DEL_REPOSITORIO`

**2. Instalar las dependencias**

Es necesario tener Python instalado. Ejecutar:

`python -m pip install numpy matplotlib`

**3. Ejecutar las simulaciones**

Para visualizar las líneas del campo eléctrico:

`python problema1.py`

Para realizar el análisis de sensibilidad eléctrica:

`python sensibilidad1.py`

Para visualizar las líneas del campo magnético:

`python problema2.py`

Para realizar el análisis de sensibilidad magnética:

`python sensibilidad2.py`

Los programas generan las representaciones gráficas correspondientes y muestran los resultados numéricos en la terminal.

---

## Análisis de los resultados

Las simulaciones permiten comprobar la aplicación de las condiciones de frontera electromagnéticas.

En el problema dieléctrico se observa que la componente tangencial del campo eléctrico permanece continua al atravesar la interfaz, mientras que la componente normal experimenta una variación asociada a las permitividades de los materiales y a la carga superficial libre.

En el problema magnético se verifica la continuidad de la componente normal de la densidad de flujo magnético y la discontinuidad de la componente tangencial de la intensidad del campo magnético, determinada por la corriente superficial libre.

Los análisis de sensibilidad muestran cómo las propiedades electromagnéticas de los medios y las fuentes superficiales modifican las magnitudes y direcciones de los campos.

Las representaciones gráficas utilizan proyecciones bidimensionales de campos tridimensionales, conservando las relaciones entre sus componentes y los ángulos respecto a las normales de las interfaces.

## Conclusiones

1. Las condiciones de frontera permiten relacionar los campos electromagnéticos de dos medios materiales y describir su comportamiento en la superficie de separación.

2. Las diferencias de permitividad y permeabilidad producen cambios en la dirección de los campos eléctricos y magnéticos.

3. La presencia de cargas y corrientes superficiales libres introduce discontinuidades específicas que deben considerarse en el análisis de las interfaces.

4. Los análisis de sensibilidad permiten identificar la influencia de los parámetros físicos sobre las componentes de los campos y sus ángulos de refracción.

5. Python constituye una herramienta útil para verificar resultados analíticos, representar fenómenos electromagnéticos y complementar su interpretación física.

---

## Información académica

Este repositorio forma parte del **Taller Grupal de Teoría Electromagnética** de la Facultad de Minas de la Universidad Nacional de Colombia, sede Medellín.

El desarrollo computacional complementa el informe científico elaborado bajo el formato IEEE, en el cual se presentan los fundamentos teóricos, procedimientos matemáticos, resultados, simulaciones y conclusiones del trabajo.

**Docente responsable:** Gustavo Gutiérrez Rodríguez.

**Desarrollado por:** Carlos José López Bacca, Juan José Cadavid Torres y Esteban Ossa Lopera.

**Universidad Nacional de Colombia — Sede Medellín, 2026.**
