"""
Módulo para calcular volúmenes de sólidos de revolución
"""

import numpy as np
from scipy import integrate


class VolumenRevolucion:
    """Calcula volúmenes usando el método de discos/anillos"""
    
    def __init__(self):
        """Inicializa el calculador de volúmenes"""
        pass
    
    def volumen_disco(self, func, a, b, n=1000):
        """
        Calcula volumen rotando alrededor del eje X
        V = π ∫[a,b] [f(x)]² dx
        
        Args:
            func: función a rotar
            a: límite inferior
            b: límite superior
            n: número de divisiones
            
        Returns:
            Volumen del sólido
        """
        def integrando(x):
            return np.pi * func(x)**2
        
        volumen, _ = integrate.quad(integrando, a, b)
        return volumen
    
    def volumen_anillo(self, func_externa, func_interna, a, b, n=1000):
        """
        Calcula volumen entre dos funciones rotadas alrededor del eje X
        V = π ∫[a,b] {[f_ext(x)]² - [f_int(x)]²} dx
        
        Args:
            func_externa: función externa
            func_interna: función interna
            a: límite inferior
            b: límite superior
            
        Returns:
            Volumen del sólido
        """
        def integrando(x):
            return np.pi * (func_externa(x)**2 - func_interna(x)**2)
        
        volumen, _ = integrate.quad(integrando, a, b)
        return volumen
    
    def volumen_capas_cilindricas(self, func, a, b, n=1000):
        """
        Calcula volumen usando método de capas cilíndricas
        V = 2π ∫[a,b] x * f(x) dx
        
        Args:
            func: función a rotar
            a: límite inferior
            b: límite superior
            
        Returns:
            Volumen del sólido
        """
        def integrando(x):
            return 2 * np.pi * x * func(x)
        
        volumen, _ = integrate.quad(integrando, a, b)
        return volumen
