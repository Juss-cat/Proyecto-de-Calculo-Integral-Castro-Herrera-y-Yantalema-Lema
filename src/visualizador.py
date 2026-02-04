"""
Módulo de visualización para gráficos
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches


class Visualizador:
    """Visualiza funciones e integrales"""
    
    def __init__(self):
        """Inicializa el visualizador"""
        pass
    
    def graficar_funcion(self, func, a, b, titulo="Gráfico de función", label="f(x)"):
        """
        Grafica una función
        
        Args:
            func: función a graficar
            a: límite inferior
            b: límite superior
            titulo: título del gráfico
            label: etiqueta de la función
        """
        x = np.linspace(a, b, 1000)
        y = func(x)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=label)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(titulo)
        plt.legend()
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        plt.show()
    
    def graficar_area_bajo_curva(self, func, a, b, n=100):
        """
        Grafica el área bajo una curva
        
        Args:
            func: función
            a: límite inferior
            b: límite superior
            n: número de rectángulos
        """
        x = np.linspace(a, b, 1000)
        y = func(x)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
        
        # Llenar el área bajo la curva
        x_fill = np.linspace(a, b, n)
        y_fill = func(x_fill)
        plt.fill_between(x_fill, 0, y_fill, alpha=0.3, color='blue', label='Área')
        
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Área bajo la curva de {a} a {b}')
        plt.legend()
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        plt.show()
    
    def graficar_volumen_revolucion(self, func, a, b, titulo="Sólido de revolución"):
        """
        Grafica una función que será rotada (visualización 2D)
        
        Args:
            func: función a rotar
            a: límite inferior
            b: límite superior
            titulo: título del gráfico
        """
        x = np.linspace(a, b, 1000)
        y = func(x)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Gráfico de la función original
        ax1.plot(x, y, 'b-', linewidth=2)
        ax1.fill_between(x, 0, y, alpha=0.3)
        ax1.axhline(y=0, color='k', linewidth=0.5)
        ax1.axvline(x=0, color='k', linewidth=0.5)
        ax1.grid(True, alpha=0.3)
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_title('Función original')
        
        # Visualización de rotación
        theta = np.linspace(0, 2*np.pi, 100)
        for x_val in np.linspace(a, b, 10):
            y_val = func(x_val)
            z = y_val * np.cos(theta)
            y_rot = y_val * np.sin(theta)
            ax2.plot(z, y_rot, 'b-', alpha=0.3)
        
        ax2.set_xlabel('z')
        ax2.set_ylabel('y')
        ax2.set_title('Sólido de revolución (vista superior)')
        ax2.axis('equal')
        ax2.grid(True, alpha=0.3)
        
        plt.suptitle(titulo)
        plt.tight_layout()
        plt.show()
