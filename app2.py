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

if "flujo_caja" not in st.session_state:
    st.session_state.flujo_caja = []

# ==========================================================
# FUNCIÓN HOME
# ==========================================================

def home():

    st.title("📦 Sistema de Gestión Logística")

    st.markdown("---")

    st.image("images.png", use_container_width=True)

    st.markdown("---")

    st.header("📖 Descripción del Proyecto")

    st.write("""
Este proyecto fue desarrollado utilizando **Python**, **Streamlit**,
**NumPy** y **Pandas** como parte del curso **Python Fundamentals**.

El objetivo es implementar una aplicación web que permita resolver
cuatro ejercicios aplicando funciones, programación orientada a objetos,
manejo de arreglos y estructuras de datos.
""")

    st.markdown("---")

    st.header("🛠 Tecnologías utilizadas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Lenguaje", "Python")

    with col2:
        st.metric("Framework", "Streamlit")

    with col3:
        st.metric("Librerías", "NumPy / Pandas")

    st.markdown("---")

    st.header("📚 Módulos del Sistema")

    c1, c2 = st.columns(2)

    with c1:

        st.success("💰 Flujo de Caja")

        st.write("""
Registro de ingresos y gastos para calcular
automáticamente el saldo disponible.
""")

        st.success("📋 Registro de Productos")

        st.write("""
Administración de productos utilizando
NumPy y Pandas.
""")

    with c2:

        st.success("📊 Costo Unitario Total")

        st.write("""
Uso de funciones de Python para calcular
el costo unitario de productos.
""")

        st.success("📦 Gestión de Inventario")

        st.write("""
CRUD utilizando Programación Orientada
a Objetos.
""")

    st.markdown("---")

    st.info("Seleccione un módulo desde el menú lateral.")

# ==========================================================
# EJERCICIO 1
# ==========================================================

def flujo_caja():

    st.title("💰 Flujo de Caja")

    st.markdown("---")

    st.write("""
En este módulo se registrarán los ingresos y gastos
para calcular automáticamente el saldo final.
""")

    st.info("🚧 Este módulo será desarrollado en la Parte 2.")

# ==========================================================
# EJERCICIO 2
# ==========================================================

def registro_productos():

    st.title("📋 Registro de Productos")

    st.markdown("---")

    st.write("""
En este módulo se registrarán productos
empleando NumPy y Pandas.
""")

    st.info("🚧 Este módulo será desarrollado en la Parte 3.")

# ==========================================================
# EJERCICIO 3
# ==========================================================

def costo_unitario():

    st.title("📊 Costo Unitario Total")

    st.markdown("---")

    st.write("""
En este módulo se utilizará la función
calcular_costo_unitario_total().
""")

    st.info("🚧 Este módulo será desarrollado en la Parte 4.")

# ==========================================================
# EJERCICIO 4
# ==========================================================

def gestion_inventario():

    st.title("📦 Gestión de Inventario")

    st.markdown("---")

    st.write("""
En este módulo se implementará un CRUD
utilizando la clase InventarioProducto.
""")

    st.info("🚧 Este módulo será desarrollado en la Parte 5.")
    st.markdown("---")

    st.info("Aquí construiremos el CRUD usando InventarioProducto en la Parte 5.")
    # ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("📦 Sistema de Gestión Logística")

st.sidebar.markdown("---")

st.sidebar.markdown("## 📋 Menú Principal")

opcion = st.sidebar.radio(
    "Seleccione un módulo",
    (
        "🏠 Inicio",
        "💰 Flujo de Caja",
        "📋 Registro de Productos",
        "📊 Costo Unitario Total",
        "📦 Gestión de Inventario"
    )
)

st.sidebar.markdown("---")

st.sidebar.subheader("👨‍💻 Información")

st.sidebar.write("**Autor:**")
st.sidebar.write("Luis Fernando Valverde Mendoza")

st.sidebar.write("**Curso:**")
st.sidebar.write("Python Fundamentals")

st.sidebar.write("**Aplicación:**")
st.sidebar.write("Sistema de Gestión Logística")

st.sidebar.markdown("---")

st.sidebar.success("✅ Proyecto desarrollado con Streamlit")

# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

if opcion == "🏠 Inicio":
    home()

elif opcion == "💰 Flujo de Caja":
    flujo_caja()

elif opcion == "📋 Registro de Productos":
    registro_productos()

elif opcion == "📊 Costo Unitario Total":
    costo_unitario()

elif opcion == "📦 Gestión de Inventario":
    gestion_inventario()
