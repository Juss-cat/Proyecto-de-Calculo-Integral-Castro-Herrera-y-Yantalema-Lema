"""
Interfaz Web - Calculadora de Integrales (Streamlit)
Versión web pública de la aplicación
"""

import streamlit as st
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.calculadora_integrales import CalculadoraIntegrales
from src.volumen_revolucion import VolumenRevolucion
from src.longitud_arco import LongitudArco
from src.visualizador import Visualizador

# Configuración de Streamlit
st.set_page_config(page_title="Calculadora de Integrales", layout="wide")

# Título principal
st.title("📐 Calculadora de Integrales")
st.markdown("---")

# Barra lateral para seleccionar modo
modo = st.sidebar.radio(
    "Selecciona una opción:",
    ["Integral Definida", "Longitud de Arco", "Volumen de Revolución", "Ayuda"]
)

# ==================== INTEGRAL DEFINIDA ====================
if modo == "Integral Definida":
    st.header("Integral Definida")
    
    col1, col2 = st.columns(2)
    
    with col1:
        expresion = st.text_input(
            "Ingresa la función (ej: x**2 + 3*x)",
            value="x**2"
        )
        limite_inferior = st.number_input("Límite inferior", value=0.0)
        limite_superior = st.number_input("Límite superior", value=1.0)
    
    with col2:
        metodo = st.selectbox(
            "Método de integración",
            ["quad", "trapz", "simpson"]
        )
        num_puntos = st.slider("Número de puntos", 10, 1000, 100)
    
    if st.button("🔢 Calcular Integral", key="btn_integral"):
        try:
            calc = CalculadoraIntegrales()
            resultado = calc.integrar(expresion, limite_inferior, limite_superior, metodo)
            
            st.success(f"✅ Resultado: **{resultado:.6f}**")
            
            # Visualizar
            x = np.linspace(limite_inferior, limite_superior, num_puntos)
            y = eval(expresion.replace('^', '**'), {"x": x, "np": np})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(x, y, 'b-', linewidth=2, label=f"f(x) = {expresion}")
            ax.fill_between(x, 0, y, alpha=0.3, color='blue')
            ax.set_xlabel("x", fontsize=12)
            ax.set_ylabel("f(x)", fontsize=12)
            ax.set_title("Visualización de la Integral", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ==================== LONGITUD DE ARCO ====================
elif modo == "Longitud de Arco":
    st.header("Longitud de Arco")
    
    col1, col2 = st.columns(2)
    
    with col1:
        expresion = st.text_input(
            "Ingresa la función y = f(x)",
            value="x**2"
        )
        limite_inferior = st.number_input("x inicial", value=0.0)
        limite_superior = st.number_input("x final", value=1.0)
    
    with col2:
        num_puntos = st.slider("Número de puntos para precisión", 50, 500, 100)
        metodo = st.selectbox("Método numérico", ["quad", "trapz"])
    
    if st.button("📏 Calcular Longitud", key="btn_arco"):
        try:
            arco = LongitudArco()
            longitud = arco.calcular_longitud(expresion, limite_inferior, limite_superior, metodo)
            
            st.success(f"✅ Longitud de arco: **{longitud:.6f}** unidades")
            
            # Visualizar curva
            x = np.linspace(limite_inferior, limite_superior, num_puntos)
            y = eval(expresion.replace('^', '**'), {"x": x, "np": np})
            
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(x, y, 'r-', linewidth=2.5, label=f"y = {expresion}")
            ax.scatter(x[::10], y[::10], color='red', s=30, alpha=0.6)
            ax.set_xlabel("x", fontsize=12)
            ax.set_ylabel("y", fontsize=12)
            ax.set_title("Curva - Longitud de Arco", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ==================== VOLUMEN DE REVOLUCIÓN ====================
elif modo == "Volumen de Revolución":
    st.header("Volumen de Revolución")
    
    col1, col2 = st.columns(2)
    
    with col1:
        expresion = st.text_input(
            "Ingresa la función",
            value="x"
        )
        limite_inferior = st.number_input("Límite inferior", value=0.0)
        limite_superior = st.number_input("Límite superior", value=2.0)
    
    with col2:
        eje = st.selectbox("Eje de revolución", ["x", "y"])
        metodo = st.selectbox("Método", ["disco", "corteza"])
    
    if st.button("🎯 Calcular Volumen", key="btn_volumen"):
        try:
            volumen_calc = VolumenRevolucion()
            volumen = volumen_calc.calcular_volumen(expresion, limite_inferior, limite_superior, eje, metodo)
            
            st.success(f"✅ Volumen: **{volumen:.6f}** unidades³")
            
            # Visualización 2D
            x = np.linspace(limite_inferior, limite_superior, 200)
            y = eval(expresion.replace('^', '**'), {"x": x, "np": np})
            
            fig = plt.figure(figsize=(12, 5))
            
            # Gráfico 2D
            ax1 = fig.add_subplot(121)
            ax1.plot(x, y, 'g-', linewidth=2.5)
            ax1.fill_between(x, 0, y, alpha=0.3, color='green')
            ax1.axhline(y=0, color='k', linewidth=0.5)
            ax1.axvline(x=0, color='k', linewidth=0.5)
            ax1.set_xlabel("x", fontsize=12)
            ax1.set_ylabel("y", fontsize=12)
            ax1.set_title(f"Función: y = {expresion}", fontsize=12, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            
            # Gráfico 3D (rotación)
            ax2 = fig.add_subplot(122, projection='3d')
            theta = np.linspace(0, 2*np.pi, 50)
            x_rev = np.linspace(limite_inferior, limite_superior, 50)
            Theta, X = np.meshgrid(theta, x_rev)
            
            if eje == "x":
                Y = eval(expresion.replace('^', '**'), {"x": X, "np": np}) * np.cos(Theta)
                Z = eval(expresion.replace('^', '**'), {"x": X, "np": np}) * np.sin(Theta)
            else:
                Y = eval(expresion.replace('^', '**'), {"x": X, "np": np})
                Z = X
            
            ax2.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
            ax2.set_xlabel("x")
            ax2.set_ylabel("y")
            ax2.set_zlabel("z")
            ax2.set_title(f"Revolución alrededor del eje {eje.upper()}", fontsize=12, fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ==================== AYUDA ====================
elif modo == "Ayuda":
    st.header("📚 Ayuda y Guía")
    
    st.subheader("¿Cómo usar la Calculadora?")
    
    st.markdown("""
    ### **Integral Definida**
    - Calcula el área bajo una curva entre dos límites
    - Ejemplo: `x**2 + 3*x` entre 0 y 1
    - Métodos: quad (recomendado), trapz, simpson
    
    ### **Longitud de Arco**
    - Calcula la distancia a lo largo de una curva
    - Fórmula: ∫√(1 + (dy/dx)²) dx
    - Útil para física e ingeniería
    
    ### **Volumen de Revolución**
    - Calcula el volumen cuando una función se rota alrededor de un eje
    - Métodos: Disco y Corteza
    - Visualización 3D incluida
    
    ### **Sintaxis**
    - Usa `x` para la variable
    - `**` para potencias (x**2 = x²)
    - `*` para multiplicación
    - Funciones: `sin(x)`, `cos(x)`, `exp(x)`, `log(x)`, etc.
    
    ### **Ejemplos**
    | Función | Descripción |
    |---------|-------------|
    | `x**2` | Parábola |
    | `sin(x)` | Seno |
    | `exp(-x)` | Exponencial |
    | `1/(1+x**2)` | Función racional |
    """)
    
    st.info("✨ Todos los cálculos usan métodos numéricos de alta precisión (scipy.integrate)")

# Footer
st.markdown("---")
st.markdown("📊 Calculadora de Integrales © 2024 | Powered by Streamlit")
