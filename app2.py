# ==========================================================
# SISTEMA DE GESTIÓN LOGÍSTICA
# Autor: Luis Fernando Valverde Mendoza
# Curso: Python Fundamentals
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np

from libreria_funciones_proyecto1 import calcular_costo_unitario_total
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

    st.title("📊 Cálculo de Costo Unitario Total")

    st.markdown("---")

    st.write("""
Este módulo utiliza la función **calcular_costo_unitario_total()**
de la librería externa proporcionada por el curso.
""")

    if "historial_costos" not in st.session_state:
        st.session_state.historial_costos = []

    with st.form("form_costo"):

        producto = st.text_input("Nombre del producto")

        materiales = st.number_input(
            "Costo de materiales (S/.)",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        mano_obra = st.number_input(
            "Costo de mano de obra (S/.)",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        costos_indirectos = st.number_input(
            "Costos indirectos (S/.)",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        unidades = st.number_input(
            "Unidades producidas",
            min_value=1,
            step=1
        )

        calcular = st.form_submit_button("🧮 Calcular")

    if calcular:

        try:

            resultado = calcular_costo_unitario_total(
                materiales,
                mano_obra,
                costos_indirectos,
                unidades
            )

            st.success("Cálculo realizado correctamente.")

            c1, c2 = st.columns(2)

            with c1:
                st.metric(
                    "💰 Costo Total",
                    f"S/ {resultado['costo_total']:,.2f}"
                )

            with c2:
                st.metric(
                    "📦 Costo Unitario",
                    f"S/ {resultado['costo_unitario']:,.2f}"
                )

            registro = {
                "Producto": producto,
                "Materiales": materiales,
                "Mano de Obra": mano_obra,
                "Costos Indirectos": costos_indirectos,
                "Unidades": unidades,
                "Costo Total": resultado["costo_total"],
                "Costo Unitario": resultado["costo_unitario"]
            }

            st.session_state.historial_costos.append(registro)

        except Exception as e:
            st.error(str(e))

    st.markdown("---")

    if len(st.session_state.historial_costos) > 0:

        st.subheader("📋 Historial de Cálculos")

        df = pd.DataFrame(st.session_state.historial_costos)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        if st.button("🗑 Limpiar Historial"):

            st.session_state.historial_costos = []

            st.rerun()

    else:

        st.info("Aún no se han realizado cálculos.")

# ==========================================================
# EJERCICIO 4
# ==========================================================

def gestion_inventario():

    st.title("📦 Gestión de Inventario")

    st.markdown("---")

    st.write("""
Este módulo utiliza la clase **InventarioProducto**
de la librería del proyecto para calcular automáticamente
los indicadores del inventario.
""")

    if "gestion_inventario" not in st.session_state:
        st.session_state.gestion_inventario = []

    with st.form("form_inventario"):

        nombre = st.text_input("Nombre del Producto")

        costo = st.number_input(
            "Costo Unitario (S/.)",
            min_value=0.01,
            step=1.0,
            format="%.2f"
        )

        precio = st.number_input(
            "Precio de Venta (S/.)",
            min_value=0.01,
            step=1.0,
            format="%.2f"
        )

        stock = st.number_input(
            "Stock Actual",
            min_value=0,
            step=1
        )

        stock_minimo = st.number_input(
            "Stock Mínimo",
            min_value=0,
            step=1
        )

        guardar = st.form_submit_button("💾 Registrar")

    if guardar:

        try:

            producto = InventarioProducto(
                nombre,
                costo,
                precio,
                stock,
                stock_minimo
            )

            resumen = producto.resumen()

            st.session_state.gestion_inventario.append(resumen)

            st.success("Producto registrado correctamente.")

        except Exception as e:

            st.error(str(e))

    st.markdown("---")

    if len(st.session_state.gestion_inventario) > 0:

        df = pd.DataFrame(st.session_state.gestion_inventario)

        st.subheader("📋 Inventario")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "📦 Productos",
                len(df)
            )

        with c2:

            st.metric(
                "💰 Valor Total",
                f"S/ {df['valor_inventario'].sum():,.2f}"
            )

        with c3:

            reposicion = df["necesita_reposicion"].sum()

            st.metric(
                "⚠ Reposición",
                int(reposicion)
            )

        st.markdown("---")

        if st.button("🗑 Limpiar Inventario"):

            st.session_state.gestion_inventario = []

            st.rerun()

    else:

        st.info("No existen productos registrados.")
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
