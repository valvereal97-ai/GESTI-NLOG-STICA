# ==========================================================
# SISTEMA DE GESTIÓN LOGÍSTICA
# Autor: Luis Fernando Valverde Mendoza
# Curso: Python Fundamentals
# ==========================================================

# ==========================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================

import streamlit as st
import pandas as pd
import numpy as np

# Librerías del proyecto
from libreria_funciones_proyecto1 import *
from libreria_clases_proyecto1 import InventarioProducto


# ==========================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Sistema de Gestión Logística",
    page_icon="📦",
    layout="wide"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "productos" not in st.session_state:
    st.session_state.productos = []

if "inventario" not in st.session_state:
    st.session_state.inventario = []


# ==========================================================
# BARRA LATERAL
# ==========================================================

st.sidebar.title("📦 Sistema de Gestión Logística")

st.sidebar.markdown("---")

opcion = st.sidebar.radio(
    "Seleccione una opción",
    (
        "🏠 Home",
        "💰 Ejercicio 1",
        "📋 Ejercicio 2",
        "📊 Ejercicio 3",
        "📦 Ejercicio 4"
    )
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
Proyecto desarrollado para el curso
Python Fundamentals.

Autor:

Luis Fernando Valverde Mendoza
"""
)

# ==========================================================
# HOME
# ==========================================================

if opcion == "🏠 Home":

    st.title("📦 Sistema de Gestión Logística")

    st.write("")

    # =====================================================
    # CAMBIAR ESTA IMAGEN
    # =====================================================
    #
    # Solo reemplaza el archivo:
    #
    # imagenes/logo.png
    #
    # por la imagen que tú prefieras.
    #
    # =====================================================

    st.image(
        "imagenes/logo.png",
        width=650
    )

    st.write("")

    st.header("Descripción")

    st.write(
        """
Este proyecto fue desarrollado utilizando Python y Streamlit
como parte del curso **Python Fundamentals**.

El sistema integra cuatro ejercicios relacionados con procesos
administrativos y logísticos.

Cada módulo fue diseñado para aplicar programación en Python
mediante funciones, clases, estructuras de datos y visualización
de información.
"""
    )

    st.write("")

    st.header("Tecnologías utilizadas")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Lenguaje",
            "Python"
        )

    with col2:

        st.metric(
            "Framework",
            "Streamlit"
        )

    with col3:

        st.metric(
            "Librerías",
            "NumPy / Pandas"
        )

    st.write("")

    st.header("Módulos del proyecto")

    c1, c2 = st.columns(2)

    with c1:

        st.success("✔ Ejercicio 1")
        st.write("Flujo de Caja")

        st.success("✔ Ejercicio 2")
        st.write("Registro de Productos")

    with c2:

        st.success("✔ Ejercicio 3")
        st.write("Costo Unitario Total")

        st.success("✔ Ejercicio 4")
        st.write("CRUD de Inventario")

    st.write("")

    st.info(
        """
Seleccione una opción desde el menú lateral para comenzar.
"""
    )

# ==========================================================
# EJERCICIO 1
# ==========================================================

elif opcion == "💰 Ejercicio 1":

    st.title("💰 Ejercicio 1")

    st.write(
        "Aquí se desarrollará el Flujo de Caja."
    )


# ==========================================================
# EJERCICIO 2
# ==========================================================

elif opcion == "📋 Ejercicio 2":

    st.title("📋 Ejercicio 2")

    st.write(
        "Aquí se desarrollará el Registro de Productos."
    )


# ==========================================================
# EJERCICIO 3
# ==========================================================

elif opcion == "📊 Ejercicio 3":

    st.title("📊 Ejercicio 3")

    st.write(
        "Aquí se desarrollará el cálculo del Costo Unitario Total."
    )


# ==========================================================
# EJERCICIO 4
# ==========================================================

elif opcion == "📦 Ejercicio 4":

    st.title("📦 Ejercicio 4")

    st.write(
        "Aquí se desarrollará el CRUD de Inventario."
    )