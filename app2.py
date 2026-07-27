# ==========================================================
# SISTEMA DE GESTIÓN LOGÍSTICA
# Autor: Luis Fernando Valverde Mendoza
# Curso: Python Fundamentals
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np

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

# ==========================================================
# SIDEBAR
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

st.sidebar.success("Python Fundamentals")

st.sidebar.write("Autor:")

st.sidebar.write("Luis Fernando Valverde Mendoza")

# ==========================================================
# HOME
# ==========================================================

if opcion == "🏠 Home":

    st.title("📦 Sistema de Gestión Logística")

    st.markdown("---")

    # ==================================================
    # CAMBIAR ESTA IMAGEN
    #
    # Coloca una imagen llamada:
    #
    # imagenes/logo.png
    #
    # o cambia la ruta por la que desees.
    # ==================================================

    try:
        st.image("imagenes/logo.png", width=700)
    except:
        st.info("📷 Aquí irá la imagen principal del proyecto.")

    st.markdown("---")

    st.header("Descripción del Proyecto")

    st.write("""
Este proyecto fue desarrollado utilizando **Python** y **Streamlit**
como parte del curso **Python Fundamentals**.

El objetivo es desarrollar una aplicación que permita resolver
cuatro ejercicios utilizando funciones, clases,
NumPy, Pandas y Streamlit.
""")

    st.markdown("---")

    st.header("Tecnologías utilizadas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Lenguaje", "Python")

    with col2:
        st.metric("Framework", "Streamlit")

    with col3:
        st.metric("Librerías", "NumPy / Pandas")

    st.markdown("---")

    st.header("Módulos")

    c1, c2 = st.columns(2)

    with c1:

        st.success("💰 Ejercicio 1")
        st.write("Flujo de Caja")

        st.success("📋 Ejercicio 2")
        st.write("Registro de Productos")

    with c2:

        st.success("📊 Ejercicio 3")
        st.write("Costo Unitario Total")

        st.success("📦 Ejercicio 4")
        st.write("CRUD Inventario")

    st.markdown("---")

    st.info("Seleccione una opción desde el menú lateral.")

# ==========================================================
# EJERCICIO 1
# ==========================================================

elif opcion == "💰 Ejercicio 1":

    st.title("💰 Ejercicio 1")

    st.markdown("---")

    st.info("Aquí construiremos el Flujo de Caja en la Parte 2.")

# ==========================================================
# EJERCICIO 2
# ==========================================================

elif opcion == "📋 Ejercicio 2":

    st.title("📋 Ejercicio 2")

    st.markdown("---")

    st.info("Aquí construiremos el Registro de Productos en la Parte 3.")

# ==========================================================
# EJERCICIO 3
# ==========================================================

elif opcion == "📊 Ejercicio 3":

    st.title("📊 Ejercicio 3")

    st.markdown("---")

    st.info("Aquí utilizaremos la función calcular_costo_unitario_total() en la Parte 4.")

# ==========================================================
# EJERCICIO 4
# ==========================================================

elif opcion == "📦 Ejercicio 4":

    st.title("📦 Ejercicio 4")

    st.markdown("---")

    st.info("Aquí construiremos el CRUD usando InventarioProducto en la Parte 5.")
    )
