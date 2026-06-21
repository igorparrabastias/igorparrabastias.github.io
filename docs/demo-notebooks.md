# Cómo ejecutar los notebooks

Todos los notebooks del sitio se **renderizan aquí** (los ves bajo cada sección temática:
Fundamentos de Python, Estructuras, Algoritmos, Matemáticas). Si además quieres
**ejecutarlos** —tocar el código y ver resultados— estas son tus opciones, usando como
muestra **`notebook/python-repaso-basico/slicing.ipynb`**.

## 1. Google Colab — ejecutable, cero infraestructura

Abre el notebook ejecutable en el navegador (solo requiere cuenta Google):

[:material-google: Abrir en Colab](https://colab.research.google.com/github/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/python-repaso-basico/slicing.ipynb){ .md-button .md-button--primary target=_blank }

!!! note "Cómo se ve la URL"
    `https://colab.research.google.com/github/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/<ruta>.ipynb`

## 2. Binder — ejecuta el repo completo en la nube

Arranca un entorno Jupyter real con todo el repositorio (más lento de iniciar, ~1-2 min):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/igorparrabastias/igorparrabastias.github.io/HEAD?labpath=notebook/python-repaso-basico/slicing.ipynb){ target=_blank }

## 3. nbviewer — vista limpia (solo lectura)

Renderiza el notebook con sus salidas, sin ejecutar (bueno para leer/compartir):

[:material-eye: Ver en nbviewer](https://nbviewer.org/github/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/python-repaso-basico/slicing.ipynb){ .md-button target=_blank }

## 4. mkdocs-jupyter — renderizado DENTRO de este sitio

El notebook se ve como una página más del sitio (mismo estilo Material), con sus salidas:

[:material-notebook: Ver render inline](demo/slicing.ipynb){ .md-button }

---

## Resumen

| Opción | Ejecutable | Dentro del sitio | Esfuerzo | Mejor para |
|---|---|---|---|---|
| **Colab** | ✅ (Google) | ❌ (abre fuera) | nulo | que alumnos *ejecuten* |
| **Binder** | ✅ (repo entero) | ❌ | nulo | sesión real efímera |
| **nbviewer** | ❌ (lectura) | ❌ | nulo | leer/compartir |
| **mkdocs-jupyter** | ❌ (lectura) | ✅ | bajo | integrarlo al sitio |

**Recomendación:** **mkdocs-jupyter** (verlo dentro del sitio) **+ botón "Abrir en Colab"** arriba de cada
notebook. Así se lee con el estilo del sitio y se ejecuta con un clic, sin cambiar de dominio.
