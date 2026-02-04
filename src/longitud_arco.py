"""
Módulo para calcular longitud de arco
"""

import numpy as np
from scipy import integrate


class LongitudArco:
    """Calcula la longitud de arco de curvas"""
    
    def __init__(self):
        """Inicializa el calculador de longitud de arco"""
        pass
    
    def longitud_arco_cartesiana(self, func, derivada, a, b):
        """
        Calcula la longitud de arco usando coordenadas cartesianas
        L = ∫[a,b] √(1 + [f'(x)]²) dx
        
        Args:
            func: función y = f(x)
            derivada: función derivada f'(x)
            a: límite inferior
            b: límite superior
            
        Returns:
            Longitud del arco
        """
        def integrando(x):
            return np.sqrt(1 + derivada(x)**2)
        
        longitud, _ = integrate.quad(integrando, a, b)
        return longitud
    
    def longitud_arco_parametrica(self, derivada_x, derivada_y, a, b):
        """
        Calcula la longitud de arco para curvas paramétricas
        L = ∫[a,b] √([dx/dt]² + [dy/dt]²) dt
        
        Args:
            derivada_x: dx/dt
            derivada_y: dy/dt
            a: parámetro inicial
            b: parámetro final
            
        Returns:
            Longitud del arco
        """
        def integrando(t):
            return np.sqrt(derivada_x(t)**2 + derivada_y(t)**2)
        
        longitud, _ = integrate.quad(integrando, a, b)
        return longitud
    
    def longitud_arco_polar(self, radio, derivada_radio, a, b):
        """
        Calcula la longitud de arco en coordenadas polares
        L = ∫[a,b] √([r]² + [dr/dθ]²) dθ
        
        Args:
            radio: función r(θ)
            derivada_radio: dr/dθ
            a: ángulo inicial
            b: ángulo final
            
        Returns:
            Longitud del arco
        """
        def integrando(theta):
            r = radio(theta)
            dr = derivada_radio(theta)
            return np.sqrt(r**2 + dr**2)
        
        longitud, _ = integrate.quad(integrando, a, b)
        return longitud
