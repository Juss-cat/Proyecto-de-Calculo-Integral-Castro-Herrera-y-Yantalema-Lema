"""
Interfaz Gráfica - Calculadora de Integrales
Versión SIMPLIFICADA sin CustomTkinter (usa tkinter básico)
ÚSALO si CustomTkinter no funciona
"""

import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import numpy as np
from scipy import integrate
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.calculadora_integrales import CalculadoraIntegrales
from src.volumen_revolucion import VolumenRevolucion
from src.longitud_arco import LongitudArco
from src.visualizador import Visualizador


class AplicacionIntegrales:
    """Aplicación con interfaz gráfica mejorada"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Integrales v2.5")
        self.root.geometry("1400x800")
        self.root.configure(bg="#fafbfc")
        
        # LOCK para evitar múltiples ejecuciones simultáneas
        self.texto_lock = threading.Lock()
        
        # Módulos
        self.calc = CalculadoraIntegrales()
        self.vol = VolumenRevolucion()
        self.long = LongitudArco()
        self.viz = Visualizador()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica"""
        # Header
        header = tk.Frame(self.root, bg="#f0f3f7", height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        header.pack_propagate(False)
        
        titulo = tk.Label(
            header,
            text="∫ CALCULADORA DE INTEGRALES v2.5",
            font=("Segoe UI", 20, "bold"),
            bg="#f0f3f7",
            fg="#c8a9e8"
        )
        titulo.pack(pady=10)
        
        # Marco principal
        marco_principal = tk.Frame(self.root, bg="#fafbfc")
        marco_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Sidebar
        self.crear_sidebar(marco_principal)
        
        # Área principal
        self.crear_area_principal(marco_principal)
    
    def crear_sidebar(self, parent):
        """Crea el sidebar izquierdo"""
        sidebar = tk.Frame(parent, bg="#ffffff", relief=tk.RIDGE, bd=2)
        sidebar.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        sidebar.pack_propagate(False)
        sidebar.configure(width=280)
        
        # Título
        titulo_menu = tk.Label(
            sidebar,
            text="MENÚ",
            font=("Segoe UI", 12, "bold"),
            bg="#f0f3f7",
            fg="#c8a9e8"
        )
        titulo_menu.pack(fill=tk.X, pady=10)
        
        # Botones principales
        botones = [
            ("📊 Integrales Definidas", self.mostrar_calculadora),
            ("🔄 Sustitución Trig.", self.mostrar_integracion_trig),
            ("📏 Longitud de Arco", self.mostrar_longitud),
            ("🌀 Volumen 3D", self.mostrar_volumen_revolucion),
        ]
        
        for texto, comando in botones:
            btn = tk.Button(
                sidebar,
                text=texto,
                command=comando,
                font=("Segoe UI", 10),
                bg="#c8a9e8",
                fg="white",
                padx=15,
                pady=10,
                relief=tk.FLAT,
                cursor="hand2",
                activebackground="#b5a7d6"
            )
            btn.pack(fill=tk.X, padx=10, pady=5)
        
        # Separador
        ttk.Separator(sidebar, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=0, pady=15)
        
        # Constructor Interactivo
        titulo_constructor = tk.Label(
            sidebar,
            text="HERRAMIENTAS",
            font=("Segoe UI", 12, "bold"),
            bg="#f0f3f7",
            fg="#c8a9e8"
        )
        titulo_constructor.pack(fill=tk.X, pady=10)
        
        btn_constructor = tk.Button(
            sidebar,
            text="🎮 Desafíos Educativos",
            command=self.abrir_desafios,
            font=("Segoe UI", 10),
            bg="#f4b5d6",
            fg="white",
            padx=15,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#f0a5d0",
            wraplength=200
        )
        btn_constructor.pack(fill=tk.X, padx=10, pady=5)
        
        # Espaciador
        tk.Frame(sidebar).pack(fill=tk.BOTH, expand=True)
        
        # Botón salir
        btn_salir = tk.Button(
            sidebar,
            text="❌ SALIR",
            command=self.root.quit,
            font=("Segoe UI", 11, "bold"),
            bg="#e8c1c1",
            fg="white",
            padx=15,
            pady=12,
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#d6a7a7"
        )
        btn_salir.pack(fill=tk.X, padx=10, pady=10)
    
    def crear_area_principal(self, parent):
        """Crea el área principal con pestañas"""
        area = tk.Frame(parent, bg="#ffffff", relief=tk.RIDGE, bd=2)
        area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Notebook
        self.notebook = ttk.Notebook(area)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Pestaña de información
        self.tab_info = tk.Frame(self.notebook, bg="#ffffff")
        self.notebook.add(self.tab_info, text="📋 Información")
        
        # Área de texto
        self.texto_info = tk.Text(
            self.tab_info,
            font=("Consolas", 10),
            bg="#ffffff",
            fg="#1a1a1a",
            wrap=tk.WORD,
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.texto_info.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de gráficos
        self.tab_grafico = tk.Frame(self.notebook, bg="#ffffff")
        self.notebook.add(self.tab_grafico, text="📈 Gráficos")
        
        # Mostrar bienvenida
        self.mostrar_bienvenida()
    
    def mostrar_bienvenida(self):
        """Muestra mensaje de bienvenida"""
        mensaje = """
╔══════════════════════════════════════════════════════════╗
║   ∫ BIENVENIDO A LA CALCULADORA DE INTEGRALES v2.5      ║
╚══════════════════════════════════════════════════════════╝

📚 MÓDULOS DISPONIBLES:

1️⃣  CALCULADORA DE INTEGRALES DEFINIDAS
    • Método de Rectángulos
    • Método de Trapecios
    • Cálculos numéricos precisos

2️⃣  INTEGRACIÓN POR SUSTITUCIÓN TRIGONOMÉTRICA
    • Identidades trigonométricas
    • Transformación automática
    • Cálculo avanzado

3️⃣  LONGITUD DE ARCO
    • Coordenadas Cartesianas
    • Parametrizaciones
    • Curvas suaves

4️⃣  VOLUMEN DE SÓLIDO DE REVOLUCIÓN (3D)
    • Método de Discos
    • Método de Capas Cilíndricas
    • Visualización tridimensional

🚀 CÓMO COMENZAR:
   1. Selecciona un módulo en el menú
   2. Ingresa los parámetros
   3. Observa los resultados
   4. Explora los gráficos

═══════════════════════════════════════════════════════════"""
        
        self.mostrar_texto_info(mensaje)
    
    def limpiar_texto_info(self):
        """Limpia completamente el área de información"""
        self.texto_info.config(state=tk.NORMAL)
        self.texto_info.delete("1.0", tk.END)
        self.texto_info.config(state=tk.DISABLED)
    
    def mostrar_texto_info(self, texto):
        """Muestra texto en el área de información de forma segura"""
        # Usar LOCK para evitar ejecuciones simultáneas
        with self.texto_lock:
            try:
                # DEBUG
                print(f"[DEBUG] Tamaño: {len(texto)} chars, Encabezados: {texto.count('╔════')}")
                
                self.texto_info.config(state=tk.NORMAL)
                self.texto_info.delete("1.0", tk.END)
                self.texto_info.insert("1.0", texto)
                self.texto_info.config(state=tk.DISABLED)
                self.root.update_idletasks()
                
                print(f"[DEBUG] Insertado OK")
            except Exception as e:
                print(f"[ERROR] mostrar_texto_info: {e}")
    
    def mostrar_calculadora(self):
        """Muestra ventana de calculadora"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Calculadora de Integrales")
        ventana.geometry("450x500")
        
        tk.Label(ventana, text="Función f(x):", font=("Arial", 10)).pack(pady=5)
        func_var = tk.StringVar(value="x**2")
        tk.Entry(ventana, textvariable=func_var, font=("Arial", 10), width=40).pack(pady=5)
        
        tk.Label(ventana, text="Límite inferior (a):", font=("Arial", 10)).pack(pady=5)
        a_var = tk.DoubleVar(value=0)
        tk.Entry(ventana, textvariable=a_var, font=("Arial", 10)).pack(pady=5)
        
        tk.Label(ventana, text="Límite superior (b):", font=("Arial", 10)).pack(pady=5)
        b_var = tk.DoubleVar(value=3)
        tk.Entry(ventana, textvariable=b_var, font=("Arial", 10)).pack(pady=5)
        
        tk.Label(ventana, text="Método:", font=("Arial", 10)).pack(pady=5)
        metodo_var = tk.StringVar(value="rectangulos")
        ttk.Combobox(ventana, textvariable=metodo_var, values=["rectangulos", "trapecios"], state="readonly").pack(pady=5)
        
        show_proc_var = tk.BooleanVar(value=True)
        tk.Checkbutton(ventana, text="Mostrar procedimiento", variable=show_proc_var).pack(pady=5)
        
        # Variable para evitar múltiples clics
        calculando = tk.BooleanVar(value=False)
        boton_calcular = None
        
        def calcular():
            # Evitar múltiples clics simultáneos
            if calculando.get():
                return
            
            calculando.set(True)
            boton_calcular.config(state=tk.DISABLED)
            
            try:
                a = a_var.get()
                b = b_var.get()
                metodo = metodo_var.get()
                func = lambda x: eval(func_var.get())
                
                if metodo == "rectangulos":
                    resultado = self.calc.metodo_rectangulos(func, a, b)
                    desc_metodo = "Método de Rectángulos"
                else:
                    resultado = self.calc.metodo_trapecios(func, a, b)
                    desc_metodo = "Método de Trapecios"
                
                # Calcular con scipy para comparar
                resultado_scipy, error_scipy = integrate.quad(func, a, b)
                error_relativo = abs(resultado - resultado_scipy) / abs(resultado_scipy) * 100 if resultado_scipy != 0 else 0
                
                texto = (
                    "╔════════════════════════════════════════════════════════╗\n"
                    "║         CÁLCULO DE INTEGRAL DEFINIDA                   ║\n"
                    "╚════════════════════════════════════════════════════════╝\n\n"
                    "📋 PARÁMETROS DE ENTRADA:\n"
                    "─" * 56 + "\n"
                    f"  Función:          f(x) = {func_var.get()}\n"
                    f"  Intervalo:        [{a}, {b}]\n"
                    f"  Rango de integración: {b - a:.4f} unidades\n"
                    f"  Método utilizado: {desc_metodo}\n\n"
                    "🔍 INTERPRETACIÓN GEOMÉTRICA:\n"
                    "─" * 56 + "\n"
                    f"  Se calcula el ÁREA bajo la curva entre x = {a} y x = {b}\n"
                    f"  Esta área representa: ∫[{a},{b}] {func_var.get()} dx\n\n"
                    "📊 RESULTADOS DEL CÁLCULO:\n"
                    "─" * 56 + "\n"
                    f"  Resultado ({desc_metodo}):  {resultado:.10f}\n"
                    f"  Resultado Exacto (scipy): {resultado_scipy:.10f}\n"
                    f"  Error relativo:           {error_relativo:.6f}%\n"
                    f"  Error absoluto:           {abs(resultado - resultado_scipy):.10f}\n\n"
                    "✅ CONCLUSIÓN:\n"
                    "─" * 56 + "\n"
                    f"  ∫[{a},{b}] f(x) dx ≈ {resultado:.6f} unidades²\n"
                    "═" * 56 + "\n"
                )
                
                self.mostrar_texto_info(texto)
                
                self.graficar_integral(func, a, b)
                self.notebook.select(0)
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                calculando.set(False)
                boton_calcular.config(state=tk.NORMAL)
        
        boton_calcular = tk.Button(ventana, text="🚀 CALCULAR", command=calcular, font=("Arial", 12), bg="#c8a9e8", fg="white", pady=10)
        boton_calcular.pack(pady=15)
    
    def mostrar_integracion_trig(self):
        """Ventana de sustitución trigonométrica"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Sustitución Trigonométrica")
        ventana.geometry("500x450")
        
        campos = [
            ("Función f(x):", "1/(x**2+1)"),
            ("Sustitución (ej: x = tan(t)):", "x = tan(t)"),
            ("Identidad:", "1 + tan²(t) = sec²(t)"),
            ("Antiderivada:", "arctan(x)"),
            ("Límite inferior (a):", "0"),
            ("Límite superior (b):", "1"),
        ]
        
        vars_dict = {}
        for label, valor in campos:
            tk.Label(ventana, text=label, font=("Arial", 10)).pack(pady=5)
            var = tk.StringVar(value=valor)
            vars_dict[label] = var
            tk.Entry(ventana, textvariable=var, font=("Arial", 10), width=40).pack(pady=5)
        
        # Variable para evitar múltiples clics
        calculando = tk.BooleanVar(value=False)
        boton_calcular = None  # Referencia al botón
        
        def calcular():
            # Evitar múltiples clics simultáneos
            if calculando.get():
                return
            
            calculando.set(True)
            boton_calcular.config(state=tk.DISABLED)  # Deshabilitar botón
            
            try:
                a = float(vars_dict["Límite inferior (a):"].get())
                b = float(vars_dict["Límite superior (b):"].get())
                func = lambda x: eval(vars_dict["Función f(x):"].get())
                sustitucion = vars_dict["Sustitución (ej: x = tan(t)):"].get()
                identidad = vars_dict["Identidad:"].get()
                antiderivada = vars_dict["Antiderivada:"].get()
                
                resultado, _ = integrate.quad(func, a, b)
                
                texto = (
                    "╔════════════════════════════════════════════════════════╗\n"
                    "║      INTEGRACIÓN POR SUSTITUCIÓN TRIGONOMÉTRICA        ║\n"
                    "╚════════════════════════════════════════════════════════╝\n\n"
                    "📋 FUNCIÓN ORIGINAL:\n"
                    "─" * 56 + "\n"
                    f"  f(x) = {vars_dict['Función f(x):'].get()}\n"
                    f"  Intervalo: [{a}, {b}]\n\n"
                    "🔄 PASO 1: SUSTITUCIÓN TRIGONOMÉTRICA\n"
                    "─" * 56 + "\n"
                    f"  {sustitucion}\n"
                    f"  Identidad utilizada: {identidad}\n\n"
                    f"📝 PASO 2: SIMPLIFICACIÓN\n"
                    "─" * 56 + "\n"
                    f"  Aplicar la identidad para simplificar la integral\n"
                    f"  La integral se reduce a una forma más simple\n\n"
                    "📊 PASO 3: ANTIDERIVADA\n"
                    "─" * 56 + "\n"
                    f"  Antiderivada encontrada: {antiderivada}\n\n"
                    "✅ RESULTADO FINAL:\n"
                    "─" * 56 + "\n"
                    f"  ∫[{a},{b}] {vars_dict['Función f(x):'].get()} dx\n"
                    f"  = [{antiderivada}] evaluada en [{a}, {b}]\n"
                    f"  = {resultado:.10f} unidades²\n"
                    "═" * 56 + "\n"
                )
                
                self.mostrar_texto_info(texto)
                self.graficar_integral(func, a, b)
                self.notebook.select(0)
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                calculando.set(False)
                boton_calcular.config(state=tk.NORMAL)  # Habilitar botón nuevamente
        
        boton_calcular = tk.Button(ventana, text="🚀 CALCULAR", command=calcular, font=("Arial", 12), bg="#c8a9e8", fg="white", pady=10)
        boton_calcular.pack(pady=15)
    
    def mostrar_longitud(self):
        """Ventana de longitud de arco"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Longitud de Arco")
        ventana.geometry("450x400")
        
        campos = [
            ("Función f(x):", "x**2/4"),
            ("Derivada f'(x):", "x/2"),
            ("Límite inferior (a):", "0"),
            ("Límite superior (b):", "4"),
        ]
        
        vars_dict = {}
        for label, valor in campos:
            tk.Label(ventana, text=label, font=("Arial", 10)).pack(pady=5)
            var = tk.StringVar(value=valor)
            vars_dict[label] = var
            tk.Entry(ventana, textvariable=var, font=("Arial", 10), width=40).pack(pady=5)
        
        # Variable para evitar múltiples clics
        calculando = tk.BooleanVar(value=False)
        boton_calcular = None
        
        def calcular():
            # Evitar múltiples clics simultáneos
            if calculando.get():
                return
            
            calculando.set(True)
            boton_calcular.config(state=tk.DISABLED)
            
            try:
                a = float(vars_dict["Límite inferior (a):"].get())
                b = float(vars_dict["Límite superior (b):"].get())
                func = lambda x: eval(vars_dict["Función f(x):"].get())
                deriv = lambda x: eval(vars_dict["Derivada f'(x):"].get())
                
                longitud = self.long.longitud_arco_cartesiana(func, deriv, a, b)
                
                # Calcular también con scipy para comparar
                integrando = lambda x: np.sqrt(1 + deriv(x)**2)
                longitud_scipy, _ = integrate.quad(integrando, a, b)
                
                texto = (
                    "╔════════════════════════════════════════════════════════╗\n"
                    "║              CÁLCULO DE LONGITUD DE ARCO               ║\n"
                    "╚════════════════════════════════════════════════════════╝\n\n"
                    "📋 FUNCIÓN Y PARÁMETROS:\n"
                    "─" * 56 + "\n"
                    f"  Función:     f(x) = {vars_dict['Función f(x):'].get()}\n"
                    f"  Derivada:    f'(x) = {vars_dict['Derivada f\'(x):'].get()}\n"
                    f"  Intervalo:   [{a}, {b}]\n\n"
                    "📐 FÓRMULA DE LONGITUD DE ARCO:\n"
                    "─" * 56 + "\n"
                    f"  L = ∫[{a},{b}] √(1 + [f'(x)]²) dx\n"
                    f"  L = ∫[{a},{b}] √(1 + [{vars_dict['Derivada f\'(x):'].get()}]²) dx\n\n"
                    "🔍 INTERPRETACIÓN:\n"
                    "─" * 56 + "\n"
                    f"  Mide la longitud total de la curva entre x = {a} y x = {b}\n"
                    f"  Como si trazaras un hilo sobre la curva y lo midieras\n\n"
                    "📊 CÁLCULO PASO A PASO:\n"
                    "─" * 56 + "\n"
                    f"  1. Calcular la derivada: f'(x) = {vars_dict['Derivada f\'(x):'].get()}\n"
                    f"  2. Elevar al cuadrado: [f'(x)]² = [...]\n"
                    f"  3. Sumar 1: 1 + [f'(x)]² = [...]\n"
                    f"  4. Sacar raíz cuadrada: √(1 + [f'(x)]²)\n"
                    f"  5. Integrar desde {a} hasta {b}\n\n"
                    "✅ RESULTADO:\n"
                    "─" * 56 + "\n"
                    f"  Longitud de arco = {longitud:.10f} unidades\n"
                    f"  Verificación:     {longitud_scipy:.10f} unidades\n"
                    "═" * 56 + "\n"
                )
                
                self.mostrar_texto_info(texto)
                self.graficar_integral(func, a, b)
                self.notebook.select(0)
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                calculando.set(False)
                boton_calcular.config(state=tk.NORMAL)
        
        boton_calcular = tk.Button(ventana, text="🚀 CALCULAR", command=calcular, font=("Arial", 12), bg="#c8a9e8", fg="white", pady=10)
        boton_calcular.pack(pady=15)
    
    def mostrar_volumen_revolucion(self):
        """Ventana de volumen de revolución"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Volumen de Revolución")
        ventana.geometry("450x450")
        
        campos = [
            ("Función f(x):", "x**2"),
            ("Límite inferior (a):", "0"),
            ("Límite superior (b):", "3"),
        ]
        
        vars_dict = {}
        for label, valor in campos:
            tk.Label(ventana, text=label, font=("Arial", 10)).pack(pady=5)
            var = tk.StringVar(value=valor)
            vars_dict[label] = var
            tk.Entry(ventana, textvariable=var, font=("Arial", 10), width=40).pack(pady=5)
        
        tk.Label(ventana, text="Método:", font=("Arial", 10)).pack(pady=5)
        metodo_var = tk.StringVar(value="disco")
        ttk.Combobox(ventana, textvariable=metodo_var, values=["disco", "capas"], state="readonly").pack(pady=5)
        
        # Variable para evitar múltiples clics
        calculando = tk.BooleanVar(value=False)
        boton_calcular = None
        
        def calcular():
            # Evitar múltiples clics simultáneos
            if calculando.get():
                return
            
            calculando.set(True)
            boton_calcular.config(state=tk.DISABLED)
            
            try:
                a = float(vars_dict["Límite inferior (a):"].get())
                b = float(vars_dict["Límite superior (b):"].get())
                metodo = metodo_var.get()
                func = lambda x: eval(vars_dict["Función f(x):"].get())
                
                if metodo == "disco":
                    volumen = self.vol.volumen_disco(func, a, b)
                    desc_metodo = "Método de Discos"
                    formula = f"V = π ∫[{a},{b}] [f(x)]² dx"
                else:
                    volumen = self.vol.volumen_capas_cilindricas(func, a, b)
                    desc_metodo = "Método de Capas Cilíndricas"
                    formula = f"V = 2π ∫[{a},{b}] x·f(x) dx"
                
                texto = (
                    "╔════════════════════════════════════════════════════════╗\n"
                    "║       CÁLCULO DE VOLUMEN DE SÓLIDO DE REVOLUCIÓN       ║\n"
                    "╚════════════════════════════════════════════════════════╝\n\n"
                    "📋 PARÁMETROS:\n"
                    "─" * 56 + "\n"
                    f"  Función:     f(x) = {vars_dict['Función f(x):'].get()}\n"
                    f"  Intervalo:   [{a}, {b}]\n"
                    f"  Método:      {desc_metodo}\n"
                    f"  Rango:       {b - a:.4f} unidades\n\n"
                    "🔄 CONCEPTO DE REVOLUCIÓN:\n"
                    "─" * 56 + "\n"
                    f"  Se rota la curva alrededor del eje X\n"
                    f"  Esto crea un sólido 3D que se visualiza a la derecha\n"
                    f"  Similar a girar una cuchara dentro de un café ☕\n\n"
                    "📐 FÓRMULA UTILIZADA:\n"
                    "─" * 56 + "\n"
                    f"  {formula}\n\n"
                    "🔍 EXPLICACIÓN DEL MÉTODO ({desc_metodo}):\n"
                    "─" * 56 + "\n"
                    f"  • Divide el sólido en {('discos apilados' if metodo == 'disco' else 'capas cilíndricas')}\n"
                    f"  • Calcula el volumen de cada elemento\n"
                    f"  • Suma todos los volúmenes usando integración\n\n"
                    "📊 CÁLCULO PASO A PASO:\n"
                    "─" * 56 + "\n"
                    f"  1. Elevar f(x) al cuadrado: [f(x)]²\n"
                    f"  2. Multiplicar por π\n"
                    f"  3. Integrar desde x = {a} hasta x = {b}\n"
                    f"  4. Evaluar los límites\n\n"
                    "✅ RESULTADO:\n"
                    "─" * 56 + "\n"
                    f"  Volumen = {volumen:.10f} unidades³\n"
                    "═" * 56 + "\n"
                )
                
                self.mostrar_texto_info(texto)
                self.graficar_volumen_3d(func, a, b)
                self.notebook.select(0)
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                calculando.set(False)
                boton_calcular.config(state=tk.NORMAL)
        
        boton_calcular = tk.Button(ventana, text="🚀 CALCULAR", command=calcular, font=("Arial", 12), bg="#c8a9e8", fg="white", pady=10)
        boton_calcular.pack(pady=15)
    
    def ejemplo_area(self):
        func = lambda x: x**2
        resultado = self.calc.metodo_trapecios(func, 0, 3)
        texto = f"Área bajo y=x² en [0,3] = {resultado:.4f}\n"
        self.mostrar_texto_info(texto)
        self.graficar_integral(func, 0, 3)
    
    def ejemplo_volumen(self):
        func = lambda x: x/3
        volumen = self.vol.volumen_disco(func, 0, 3)
        texto = f"Volumen de cono = {volumen:.4f} unidades³\n"
        self.mostrar_texto_info(texto)
        self.graficar_integral(func, 0, 3)
    
    def ejemplo_longitud(self):
        deriv_x = lambda t: -np.sin(t)
        deriv_y = lambda t: np.cos(t)
        longitud = self.long.longitud_arco_parametrica(deriv_x, deriv_y, 0, 2*np.pi)
        texto = f"Circunferencia unitaria = {longitud:.4f} ≈ 2π\n"
        self.mostrar_texto_info(texto)
    
    def ejemplo_sustitucion(self):
        func = lambda x: 1/(x**2+1)
        resultado, _ = integrate.quad(func, 0, 1)
        texto = f"∫[0,1] 1/(x²+1) dx = {resultado:.6f} ≈ π/4\n"
        self.mostrar_texto_info(texto)
        self.graficar_integral(func, 0, 1)
    
    def graficar_integral(self, func, a, b):
        """Grafica una integral"""
        for widget in self.tab_grafico.winfo_children():
            widget.destroy()
        
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        x = np.linspace(a, b, 1000)
        y = func(x)
        
        ax.plot(x, y, color="#c8a9e8", linewidth=3)
        ax.fill_between(x, 0, y, alpha=0.3, color="#c8a9e8")
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'Gráfico de {a:.2f} a {b:.2f}')
        
        canvas = FigureCanvasTkAgg(fig, master=self.tab_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def graficar_volumen_3d(self, func, a, b):
        """Grafica un volumen de revolución en 3D con colores vibrantes"""
        for widget in self.tab_grafico.winfo_children():
            widget.destroy()
        
        fig = Figure(figsize=(10, 8), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        
        # Crear la superficie de revolución
        u = np.linspace(a, b, 100)
        v = np.linspace(0, 2*np.pi, 100)
        u_grid, v_grid = np.meshgrid(u, v)
        
        # Calcular las funciones
        x_3d = u_grid
        y_3d = func(u_grid) * np.cos(v_grid)
        z_3d = func(u_grid) * np.sin(v_grid)
        
        # Usar colores del mapa viridis (arcoíris)
        surf = ax.plot_surface(x_3d, y_3d, z_3d, cmap='rainbow', alpha=0.9, edgecolor='none', shade=True)
        
        ax.set_xlabel('x', fontsize=10, fontweight='bold')
        ax.set_ylabel('y', fontsize=10, fontweight='bold')
        ax.set_zlabel('z', fontsize=10, fontweight='bold')
        ax.set_title(f'Sólido de Revolución de {a:.2f} a {b:.2f}', fontsize=12, fontweight='bold')
        
        # Agregar barra de color
        fig.colorbar(surf, ax=ax, label='Altura')
        
        canvas = FigureCanvasTkAgg(fig, master=self.tab_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def abrir_desafios(self):
        """Abre el modo desafíos educativos con gamificación"""
        ventana = tk.Toplevel(self.root)
        ventana.title("🎮 Desafíos Educativos")
        ventana.geometry("900x850")
        ventana.configure(bg="#e8dff5")
        
        # Marco principal
        marco_principal = tk.Frame(ventana, bg="#e8dff5")
        marco_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Título y puntuación
        marco_superior = tk.Frame(marco_principal, bg="#e8dff5")
        marco_superior.pack(fill=tk.X, pady=10)
        
        titulo = tk.Label(
            marco_superior,
            text="🎮 DESAFÍOS EDUCATIVOS",
            font=("Arial", 14, "bold"),
            bg="#e8dff5",
            fg="#b5a7d6"
        )
        titulo.pack(side=tk.LEFT)
        
        var_puntos = tk.IntVar(value=0)
        label_puntos = tk.Label(
            marco_superior,
            text="⭐ Puntos: 0",
            font=("Arial", 12, "bold"),
            bg="#e8dff5",
            fg="#f4b5d6"
        )
        label_puntos.pack(side=tk.RIGHT)
        
        # Selector de nivel
        marco_nivel = tk.Frame(marco_principal, bg="#f0e8f8")
        marco_nivel.pack(fill=tk.X, pady=10, padx=10)
        
        tk.Label(
            marco_nivel,
            text="Nivel:",
            bg="#f0e8f8",
            fg="#3d2d5c",
            font=("Arial", 11, "bold")
        ).pack(side=tk.LEFT, padx=10)
        
        nivel_var = tk.StringVar(value="fácil")
        
        for nivel in ["🟢 Fácil", "🟡 Medio", "🔴 Difícil"]:
            rb = tk.Radiobutton(
                marco_nivel,
                text=nivel,
                variable=nivel_var,
                value=nivel.split()[1].lower(),
                bg="#f0e8f8",
                fg="#3d2d5c",
                selectcolor="#dcc9f0",
                font=("Arial", 10)
            )
            rb.pack(side=tk.LEFT, padx=5)
        
        # Marco del desafío con scroll
        marco_desafio_contenedor = tk.LabelFrame(
            marco_principal,
            text="📝 DESAFÍO",
            font=("Arial", 11, "bold"),
            bg="#f0e8f8",
            fg="#3d2d5c",
            padx=0,
            pady=0
        )
        marco_desafio_contenedor.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Canvas con scrollbar
        canvas_desafio = tk.Canvas(
            marco_desafio_contenedor,
            bg="#f0e8f8",
            highlightthickness=0
        )
        scrollbar_desafio = tk.Scrollbar(marco_desafio_contenedor, orient="vertical", command=canvas_desafio.yview)
        marco_desafio = tk.Frame(canvas_desafio, bg="#f0e8f8")
        
        marco_desafio.bind(
            "<Configure>",
            lambda e: canvas_desafio.configure(scrollregion=canvas_desafio.bbox("all"))
        )
        
        canvas_desafio.create_window((0, 0), window=marco_desafio, anchor="nw")
        canvas_desafio.configure(yscrollcommand=scrollbar_desafio.set)
        
        canvas_desafio.pack(side="left", fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar_desafio.pack(side="right", fill="y")
        
        # Habilitar scroll con rueda del ratón
        def on_mousewheel(event):
            canvas_desafio.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas_desafio.bind_all("<MouseWheel>", on_mousewheel)
        
        label_problema = tk.Label(
            marco_desafio,
            text="Calcula el área bajo la curva",
            font=("Arial", 12, "bold"),
            bg="#f0e8f8",
            fg="#b5a7d6",
            wraplength=400
        )
        label_problema.pack(pady=20)
        
        # Canvas para gráfico
        marco_grafico = tk.Frame(marco_desafio, bg="#dcc9f0", relief=tk.SUNKEN, bd=2, height=200)
        marco_grafico.pack(fill=tk.BOTH, expand=False, pady=10)
        marco_grafico.pack_propagate(False)
        
        # Opciones múltiples
        marco_opciones = tk.LabelFrame(
            marco_desafio,
            text="🔘 OPCIONES",
            font=("Arial", 11, "bold"),
            bg="#f0e8f8",
            fg="#3d2d5c",
            padx=15,
            pady=15
        )
        marco_opciones.pack(fill=tk.X, pady=15)
        
        opcion_var = tk.StringVar(value="")
        opciones_labels = {}
        
        for letra, num in [("A", 0), ("B", 1), ("C", 2), ("D", 3)]:
            marco_opcion = tk.Frame(marco_opciones, bg="#f0e8f8")
            marco_opcion.pack(fill=tk.X, pady=8)
            
            rb = tk.Radiobutton(
                marco_opcion,
                variable=opcion_var,
                value=letra,
                bg="#f0e8f8",
                fg="#3d2d5c",
                selectcolor="#dcc9f0",
                font=("Arial", 11),
                activebackground="#f0e8f8",
                activeforeground="#3d2d5c"
            )
            rb.pack(side=tk.LEFT, padx=10)
            
            label_opcion = tk.Label(
                marco_opcion,
                text=f"{letra}) ",
                bg="#f0e8f8",
                fg="#b5a7d6",
                font=("Arial", 11, "bold")
            )
            label_opcion.pack(side=tk.LEFT, padx=5)
            
            opciones_labels[letra] = label_opcion
        
        # Botones
        marco_botones = tk.Frame(marco_principal, bg="#e8dff5")
        marco_botones.pack(fill=tk.X, pady=10)
        
        # Variables de desafío
        desafio_actual = {
            "func": None, 
            "a": 0, 
            "b": 0, 
            "respuesta": 0, 
            "tipo": "",
            "opciones": [0, 0, 0, 0]
        }
        
        def generar_desafio():
            """Genera un nuevo desafío"""
            nivel = nivel_var.get()
            
            # Generar función y parámetros según el nivel
            import random
            funciones = {
                "fácil": [
                    ("x", 0, 2),
                    ("x**2/2", 0, 2),
                    ("2*x", 1, 3),
                ],
                "medio": [
                    ("x**2", 0, 3),
                    ("sin(x)", 0, np.pi),
                    ("exp(x)/5", 0, 1),
                ],
                "difícil": [
                    ("x**3/6", 0, 2),
                    ("sin(x)*cos(x)", 0, np.pi),
                    ("x**2 + sin(x)", 0, 2),
                ]
            }
            
            func_str, a, b = random.choice(funciones[nivel])
            func = lambda x: eval(func_str)
            resultado = self.calc.metodo_trapecios(func, a, b)
            
            desafio_actual["func"] = func
            desafio_actual["a"] = a
            desafio_actual["b"] = b
            desafio_actual["respuesta"] = resultado
            desafio_actual["tipo"] = func_str
            
            # Actualizar UI
            label_problema.config(
                text=f"Calcula ∫ ({func_str}) dx en [{a:.2f}, {b:.2f}]\n\n¿Cuál es el resultado?"
            )
            opcion_var.set("")
            
            # Generar 4 opciones (1 correcta + 3 incorrectas)
            import random as rnd
            opciones_valores = [resultado]
            
            # Generar 3 opciones incorrectas con variaciones garantizadas
            factores = [0.7, 0.85, 1.15, 1.3]  # Variaciones predeterminadas
            for factor in factores[1:]:  # Saltar el primero (1.0)
                opcion_incorrecta = resultado * factor
                opciones_valores.append(opcion_incorrecta)
            
            # Mezclar las opciones
            rnd.shuffle(opciones_valores)
            desafio_actual["opciones"] = opciones_valores
            
            # Actualizar opciones en UI
            for letra, valor in zip(["A", "B", "C", "D"], opciones_valores):
                opciones_labels[letra].config(text=f"{letra}) {valor:.4f}")
            
            # Dibujar gráfico
            for widget in marco_grafico.winfo_children():
                widget.destroy()
            
            fig = Figure(figsize=(7, 2.5), dpi=100)
            ax = fig.add_subplot(111)
            
            x = np.linspace(a, b, 500)
            y = [func(xi) for xi in x]
            
            ax.plot(x, y, color="#b5a7d6", linewidth=2)
            ax.fill_between(x, 0, y, alpha=0.3, color="#f4b5d6")
            ax.grid(True, alpha=0.3)
            ax.set_facecolor("#f0e8f8")
            fig.patch.set_facecolor("#f0e8f8")
            
            canvas = FigureCanvasTkAgg(fig, master=marco_grafico)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        def verificar_respuesta():
            """Verifica la respuesta del usuario"""
            opcion_seleccionada = opcion_var.get()
            
            if not opcion_seleccionada:
                messagebox.showwarning("Error", "Selecciona una opción primero")
                return
            
            # Índice de la opción seleccionada (A=0, B=1, C=2, D=3)
            indice = ord(opcion_seleccionada) - ord('A')
            respuesta_usuario = desafio_actual["opciones"][indice]
            respuesta_correcta = desafio_actual["respuesta"]
            error = abs(respuesta_usuario - respuesta_correcta)
            
            if error < 0.01:  # Respuesta correcta
                puntos = {"fácil": 10, "medio": 25, "difícil": 50}
                puntos_ganados = puntos[nivel_var.get()]
                var_puntos.set(var_puntos.get() + puntos_ganados)
                label_puntos.config(text=f"⭐ Puntos: {var_puntos.get()}")
                
                messagebox.showinfo(
                    "¡CORRECTO! 🎉",
                    f"¡Excelente!\nRespuesta: {respuesta_correcta:.6f}\nOpción {opcion_seleccionada}\n+{puntos_ganados} puntos"
                )
            else:
                pista = f"Pista: La respuesta correcta es {respuesta_correcta:.4f}"
                messagebox.showwarning(
                    "Intenta de nuevo ❌",
                    f"No es correcto.\n{pista}\nSeleccionaste {respuesta_usuario:.4f}"
                )
            
            generar_desafio()
        
        btn_verificar = tk.Button(
            marco_botones,
            text="✓ Verificar Respuesta",
            command=verificar_respuesta,
            font=("Arial", 11, "bold"),
            bg="#b5a7d6",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.FLAT
        )
        btn_verificar.pack(side=tk.LEFT, padx=5)
        
        btn_siguiente = tk.Button(
            marco_botones,
            text="→ Siguiente Desafío",
            command=generar_desafio,
            font=("Arial", 11, "bold"),
            bg="#f4b5d6",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.FLAT
        )
        btn_siguiente.pack(side=tk.LEFT, padx=5)
        
        # Generar primer desafío
        generar_desafio()


def main():
        ventana = tk.Toplevel(self.root)
        ventana.title("🔧 Constructor Interactivo")
        ventana.geometry("900x650")
        ventana.configure(bg="#e8dff5")
        
        # Marco principal
        marco_principal = tk.Frame(ventana, bg="#e8dff5")
        marco_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Título
        titulo = tk.Label(
            marco_principal,
            text="🔧 CONSTRUCTOR INTERACTIVO",
            font=("Arial", 14, "bold"),
            bg="#e8dff5",
            fg="#b5a7d6"
        )
        titulo.pack(pady=10)
        
        # Marco de entrada
        marco_entrada = tk.LabelFrame(
            marco_principal,
            text="CONFIGURACIÓN",
            font=("Arial", 11, "bold"),
            bg="#f0e8f8",
            fg="#3d2d5c",
            padx=10,
            pady=10
        )
        marco_entrada.pack(fill=tk.X, pady=10)
        
        # Función
        tk.Label(
            marco_entrada,
            text="Función f(x):",
            bg="#f0e8f8",
            fg="#3d2d5c",
            font=("Arial", 10)
        ).pack(anchor=tk.W)
        
        entrada_func = tk.Entry(
            marco_entrada,
            font=("Arial", 10),
            bg="#dcc9f0",
            fg="#3d2d5c"
        )
        entrada_func.insert(0, "x**2")
        entrada_func.pack(fill=tk.X, pady=5)
        
        # Tipo de cálculo
        tk.Label(
            marco_entrada,
            text="Tipo de Cálculo:",
            bg="#f0e8f8",
            fg="#3d2d5c",
            font=("Arial", 10)
        ).pack(anchor=tk.W, pady=(10, 0))
        
        tipo_var = tk.StringVar(value="integral")
        combo_tipo = ttk.Combobox(
            marco_entrada,
            textvariable=tipo_var,
            values=["integral", "volumen", "longitud"],
            state="readonly",
            font=("Arial", 10)
        )
        combo_tipo.pack(fill=tk.X, pady=5)
        
        # Deslizadores
        marco_deslizadores = tk.Frame(marco_entrada, bg="#f0e8f8")
        marco_deslizadores.pack(fill=tk.X, pady=10)
        
        # Deslizador A
        tk.Label(
            marco_deslizadores,
            text="Límite a:",
            bg="#f0e8f8",
            fg="#3d2d5c"
        ).grid(row=0, column=0, sticky=tk.W)
        
        desliz_a = tk.Scale(
            marco_deslizadores,
            from_=-10,
            to=10,
            orient=tk.HORIZONTAL,
            bg="#dcc9f0",
            fg="#b5a7d6",
            troughcolor="#f0e8f8",
            highlightthickness=0
        )
        desliz_a.set(0)
        desliz_a.grid(row=0, column=1, sticky=tk.EW, padx=10)
        
        label_a = tk.Label(
            marco_deslizadores,
            text="0.00",
            bg="#f0e8f8",
            fg="#b5a7d6",
            font=("Arial", 10, "bold")
        )
        label_a.grid(row=0, column=2, sticky=tk.W)
        
        # Deslizador B
        tk.Label(
            marco_deslizadores,
            text="Límite b:",
            bg="#f0e8f8",
            fg="#3d2d5c"
        ).grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
        
        desliz_b = tk.Scale(
            marco_deslizadores,
            from_=-10,
            to=10,
            orient=tk.HORIZONTAL,
            bg="#dcc9f0",
            fg="#b5a7d6",
            troughcolor="#f0e8f8",
            highlightthickness=0
        )
        desliz_b.set(3)
        desliz_b.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=(10, 0))
        
        label_b = tk.Label(
            marco_deslizadores,
            text="3.00",
            bg="#f0e8f8",
            fg="#b5a7d6",
            font=("Arial", 10, "bold")
        )
        label_b.grid(row=1, column=2, sticky=tk.W, pady=(10, 0))
        
        marco_deslizadores.columnconfigure(1, weight=1)
        
        # Canvas gráfico
        marco_grafico = tk.Frame(
            marco_principal,
            bg="#f0e8f8",
            relief=tk.SUNKEN,
            bd=2
        )
        marco_grafico.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Resultado
        marco_resultado = tk.LabelFrame(
            marco_principal,
            text="RESULTADO",
            font=("Arial", 11, "bold"),
            bg="#f0e8f8",
            fg="#3d2d5c",
            padx=10,
            pady=10
        )
        marco_resultado.pack(fill=tk.X)
        
        texto_resultado = tk.Text(
            marco_resultado,
            height=2,
            bg="#dcc9f0",
            fg="#3d2d5c",
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        texto_resultado.pack(fill=tk.BOTH, expand=True)
        texto_resultado.config(state=tk.DISABLED)
        
        # Función para actualizar
        def actualizar():
            try:
                a = float(desliz_a.get())
                b = float(desliz_b.get())
                func_str = entrada_func.get()
                tipo = tipo_var.get()
                
                label_a.config(text=f"{a:.2f}")
                label_b.config(text=f"{b:.2f}")
                
                if a >= b:
                    texto_resultado.config(state=tk.NORMAL)
                    texto_resultado.delete("1.0", tk.END)
                    texto_resultado.insert("1.0", "❌ Error: a debe ser menor que b")
                    texto_resultado.config(state=tk.DISABLED)
                    return
                
                func = lambda x: eval(func_str)
                
                if tipo == "integral":
                    resultado = self.calc.metodo_trapecios(func, a, b)
                    texto_res = f"∫ f(x) dx = {resultado:.6f}"
                elif tipo == "volumen":
                    resultado = self.vol.volumen_disco(func, a, b)
                    texto_res = f"V = {resultado:.6f} u³"
                else:
                    deriv = lambda x: 2 * x
                    resultado = self.long.longitud_arco_cartesiana(func, deriv, a, b)
                    texto_res = f"L = {resultado:.6f} u"
                
                texto_resultado.config(state=tk.NORMAL)
                texto_resultado.delete("1.0", tk.END)
                texto_resultado.insert("1.0", f"f(x) = {func_str}\n{texto_res}")
                texto_resultado.config(state=tk.DISABLED)
                
                # Gráfico
                for widget in marco_grafico.winfo_children():
                    widget.destroy()
                
                fig = Figure(figsize=(8, 2.5), dpi=100)
                ax = fig.add_subplot(111)
                
                x = np.linspace(a, b, 500)
                y = [func(xi) for xi in x]
                
                ax.plot(x, y, color="#b5a7d6", linewidth=2)
                ax.fill_between(x, 0, y, alpha=0.3, color="#f4b5d6")
                ax.grid(True, alpha=0.3)
                ax.set_facecolor("#f0e8f8")
                fig.patch.set_facecolor("#f0e8f8")
                
                canvas = FigureCanvasTkAgg(fig, master=marco_grafico)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
                
            except Exception as e:
                texto_resultado.config(state=tk.NORMAL)
                texto_resultado.delete("1.0", tk.END)
                texto_resultado.insert("1.0", f"❌ {str(e)}")
                texto_resultado.config(state=tk.DISABLED)
        
        def on_change(*args):
            ventana.after(100, actualizar)
        
        desliz_a.config(command=lambda x: on_change())
        desliz_b.config(command=lambda x: on_change())
        entrada_func.bind("<KeyRelease>", on_change)
        combo_tipo.bind("<<ComboboxSelected>>", on_change)
        
        actualizar()


def main():
    root = tk.Tk()
    app = AplicacionIntegrales(root)
    root.mainloop()


if __name__ == "__main__":
    main()
