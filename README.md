# IDENTIFICACIÓN DE LA FORMA DE LESIONES EN MAMOGRAFÍAS MLO A PARTIR DE LA GENERACIÓN DEL ROI UTILIZANDO INTELIGENCIA ARTIFICIAL GENERATIVA

Este repositorio contiene el sistema de generación automática de gráficas desarrolladas como parte del trabajo de grado para optar al título de **Ingeniero de Sistemas**.

### 📘 *Identificación de la forma de lesiones en mamografías MLO a partir de la generación del ROI utilizando inteligencia artificial generativa*

Los gráficos se basan en los resultados de la **revisión sistemática**:

### 📄 *Revisión sistemática del uso de aprendizaje profundo en el análisis de la forma de lesiones mamarias en mamografía*

---

## 🎯 Objetivo

Visualizar y explorar gráficamente los hallazgos extraídos del análisis sistemático de artículos científicos sobre el uso de **técnicas de aprendizaje profundo** aplicadas a mamografías, especialmente en el análisis de **la forma de las lesiones**.

Este sistema permite generar automáticamente diversos tipos de gráficos académicos que resumen tendencias, frecuencias y comparaciones categóricas.

---

## 🧠 Tecnologías utilizadas

- **Python 3.10+**
- `matplotlib`
- `seaborn`
- `pandas`

Organizado en un sistema modular orientado a la reutilización por categorías y tipos de gráficos.

---

## 📁 Estructura del proyecto


```text
thesis-graphics/
├── base/                # Clases base de cada tipo de gráfico
├── categories/          # Lógica por categoría
├── data/                # Archivos de datos por categoría
├── graphics/outputs/    # Carpeta de salida
├── main.py              # Script principal de ejecución
├── requirements.txt     # Dependencias necesarias
└── README.md            # Este archivo
```

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/dpdorado/thesis-graphics.git
cd thesis-graphics

# Crear entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 📦 Requisitos

Contenido de `requirements.txt`:

```text
matplotlib
seaborn
pandas
```

## 🚀 Uso

```bash
python main.py
```

Esto generará todos los gráficos en la carpeta `graphics/outputs/`.
