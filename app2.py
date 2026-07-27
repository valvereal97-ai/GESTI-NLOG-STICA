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
Registre los movimientos de caja de la empresa.
Cada movimiento puede ser un **Ingreso** o un **Gasto**.
El sistema calculará automáticamente el saldo disponible.
""")

    st.markdown("### ➕ Registrar Movimiento")

    with st.form("form_flujo"):

        concepto = st.text_input("Concepto")

        tipo = st.selectbox(
            "Tipo de Movimiento",
            ["Ingreso", "Gasto"]
        )

        monto = st.number_input(
            "Monto (S/.)",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        agregar = st.form_submit_button("➕ Agregar Movimiento")

    if agregar:

        if concepto.strip() == "":
            st.warning("Ingrese un concepto.")

        elif monto <= 0:
            st.warning("El monto debe ser mayor que cero.")

        else:

            nuevo = {
                "Concepto": concepto,
                "Tipo": tipo,
                "Monto": monto
            }

            st.session_state.flujo_caja.append(nuevo)

            st.success("✅ Movimiento registrado correctamente.")

    st.markdown("---")

    if len(st.session_state.flujo_caja) > 0:

        df = pd.DataFrame(st.session_state.flujo_caja)

        ingresos = df[df["Tipo"] == "Ingreso"]["Monto"].sum()
        gastos = df[df["Tipo"] == "Gasto"]["Monto"].sum()
        saldo = ingresos - gastos

        st.subheader("📊 Resumen del Flujo de Caja")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💰 Total Ingresos",
                f"S/ {ingresos:,.2f}"
            )

        with col2:
            st.metric(
                "📉 Total Gastos",
                f"S/ {gastos:,.2f}"
            )

        with col3:
            st.metric(
                "💵 Saldo Final",
                f"S/ {saldo:,.2f}"
            )

        st.markdown("---")

        st.subheader("📋 Movimientos Registrados")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        if st.button("🗑 Limpiar Registros"):

            st.session_state.flujo_caja = []

            st.success("Registros eliminados correctamente.")

            st.rerun()

    else:

        st.info("No existen movimientos registrados.")

# ==========================================================
# EJERCICIO 2
# ==========================================================

def registro_productos():

    st.title("📋 Registro de Productos")

    st.markdown("---")

    st.write("""
Registre los productos del inventario.
Este módulo utiliza **NumPy** para realizar cálculos estadísticos
y **Pandas** para administrar la información registrada.
""")

    #==========================================================
    # SESSION STATE
    #==========================================================

    if "inventario" not in st.session_state:
        st.session_state.inventario = []

    st.markdown("### ➕ Registrar Producto")

    with st.form("form_producto"):

        codigo = st.text_input("Código")

        producto = st.text_input("Nombre del Producto")

        categoria = st.selectbox(
            "Categoría",
            [
                "Herramientas",
                "Electricidad",
                "Pinturas",
                "Ferretería",
                "Otros"
            ]
        )

        precio = st.number_input(
            "Precio (S/.)",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        stock = st.number_input(
            "Stock",
            min_value=0,
            step=1
        )

        guardar = st.form_submit_button("💾 Registrar Producto")

    if guardar:

        if codigo.strip() == "":
            st.warning("Ingrese el código del producto.")

        elif producto.strip() == "":
            st.warning("Ingrese el nombre del producto.")

        elif precio <= 0:
            st.warning("El precio debe ser mayor que cero.")

        else:

            nuevo = {

                "Código": codigo,
                "Producto": producto,
                "Categoría": categoria,
                "Precio": precio,
                "Stock": stock

            }

            st.session_state.inventario.append(nuevo)

            st.success("✅ Producto registrado correctamente.")

    st.markdown("---")

    if len(st.session_state.inventario) > 0:

        df = pd.DataFrame(st.session_state.inventario)

        #======================================================
        # NUMPY
        #======================================================

        precios = np.array(df["Precio"])

        precio_promedio = np.mean(precios)

        precio_maximo = np.max(precios)

        precio_minimo = np.min(precios)

        valor_total = np.sum(df["Precio"] * df["Stock"])

        cantidad = len(df)

        st.subheader("📊 Indicadores del Inventario")

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:

            st.metric(
                "📦 Productos",
                cantidad
            )

        with c2:

            st.metric(
                "💲 Precio Promedio",
                f"S/ {precio_promedio:,.2f}"
            )

        with c3:

            st.metric(
                "📈 Precio Máximo",
                f"S/ {precio_maximo:,.2f}"
            )

        with c4:

            st.metric(
                "📉 Precio Mínimo",
                f"S/ {precio_minimo:,.2f}"
            )

        with c5:

            st.metric(
                "💰 Valor Inventario",
                f"S/ {valor_total:,.2f}"
            )

        st.markdown("---")

        st.subheader("📋 Productos Registrados")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        if st.button("🗑 Limpiar Productos"):

            st.session_state.inventario = []

            st.success("Inventario eliminado correctamente.")

            st.rerun()

    else:

        st.info("No existen productos registrados.")

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
