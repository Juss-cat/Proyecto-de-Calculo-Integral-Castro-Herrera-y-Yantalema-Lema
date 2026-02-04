"""
Módulo de Calculadora de Integrales
Implementa métodos numéricos para aproximar integrales definidas
"""

import numpy as np
from scipy import integrate


class CalculadoraIntegrales:
    """Clase para calcular integrales usando métodos numéricos"""
    
    def __init__(self):
        """Inicializa la calculadora"""
        self.resultados = []
    
    def metodo_rectangulos(self, func, a, b, n=1000):
        """
        Aproxima una integral usando el método de rectángulos
        
        Args:
            func: función a integrar
            a: límite inferior
            b: límite superior
            n: número de rectángulos
            
        Returns:
            Aproximación de la integral
        """
        dx = (b - a) / n
        x = np.linspace(a, b, n)
        y = func(x)
        integral = np.sum(y) * dx
        return integral
    
    def metodo_trapecios(self, func, a, b, n=1000):
        """
        Aproxima una integral usando el método de trapecios.

        Args:
            func: función a integrar
            a: límite inferior
            b: límite superior
            n: número de trapecios

        Returns:
            Aproximación de la integral
        """
        x = np.linspace(a, b, n)
        y = func(x)
        # Implementación explícita del trapecio para máxima compatibilidad
        dx = x[1] - x[0]
        integral = np.sum((y[:-1] + y[1:]) * 0.5 * dx)
        return integral
    
    def metodo_simpson(self, func, a, b, n=1000):
        """
        (Obsoleto) Aproxima una integral usando la regla de Simpson.
        Mantiene la implementación por compatibilidad, pero el método
        ya no se recomienda ni aparece en la GUI.
        """
        integral, error = integrate.quad(func, a, b)
        return integral
    
    def calcular_integral(self, func, a, b, metodo='trapecios'):
        """
        Calcula una integral usando el método especificado
        
        Args:
            func: función a integrar
            a: límite inferior
            b: límite superior
            metodo: 'rectangulos' o 'trapecios' ("simpson" es obsoleto)
            
        Returns:
            Valor de la integral
        """
        if metodo == 'rectangulos':
            return self.metodo_rectangulos(func, a, b)
        elif metodo == 'trapecios':
            return self.metodo_trapecios(func, a, b)
        elif metodo == 'simpson':
            # Soportar por compatibilidad, pero mapear a trapecios y avisar
            import warnings
            warnings.warn("El método 'simpson' está obsoleto; use 'trapecios' o 'rectangulos'", DeprecationWarning)
            return self.metodo_trapecios(func, a, b)
        else:
            raise ValueError(f"Método {metodo} no reconocido")
