# Simulador de Aplicaciones de Integrales

## 📚 Descripción
Proyecto educativo **interactivo y completo** que implementa aplicaciones prácticas del cálculo integral usando Python. Incluye interfaz gráfica y ejemplos de laboratorio.

## ⭐ Características Principales
- ✅ **Interfaz Gráfica (GUI)** - Menú visual intuitivo
- ✅ **5 Módulos Especializados** - Calculadora, volumen, longitud, trabajo/energía, visualización
- ✅ **4 Ejemplos Completos** - Casos reales con verificación
- ✅ **Gráficos Interactivos** - Visualización en tiempo real con matplotlib
- ✅ **Métodos Numéricos** - Rectángulos, Trapecios
- 🧩 **Ejecutable Windows** - Usa `build_exe.bat` para generar un `.exe` con PyInstaller (opcional)
- 🧳 **Bundle portable** - Usa `make_portable_fixed.bat` para crear `portable_bundle/` (incluye `.venv`) y luego `run_portable.bat` para ejecutar en otra máquina (sin Internet).
- ✅ **Documentación Completa** - Guías en español

## 🎯 Temas de Cálculo Integral Cubiertos
- Integrales definidas e indefinidas
- Métodos de integración (sustitución, partes, fracciones parciales)
- Área bajo curva
- Longitud de arco
- Volumen de sólidos de revolución
- Trabajo y energía (aplicaciones físicas)

## 🚀 Inicio Rápido

### Opción 1: INTERFAZ GRÁFICA (Recomendado)
```bash
python gui.py
```
✅ Sin necesidad de escribir código
✅ Menú visual con botones
✅ Gráficos integrados

### Opción 2: Menú Interactivo
```bash
python menu.py
```

### Opción 3: Línea de Comandos
```bash
python ejemplos/ejemplo_trabajo.py
python ejemplos/ejemplo_area.py
python ejemplos/ejemplo_volumen.py
python ejemplos/ejemplo_longitud_arco.py
```

## 📁 Estructura del Proyecto
```
PROYECTO CALCULO INTEGRAL/
├── src/                         # Módulos principales (5 módulos)
│   ├── calculadora_integrales.py    # Métodos numéricos
│   ├── volumen_revolucion.py        # Sólidos de revolución
│   ├── longitud_arco.py             # Longitud de curvas
│   ├── trabajo_energia.py           # Aplicaciones físicas
│   └── visualizador.py              # Gráficos
├── ejemplos/                    # Ejemplos de laboratorio (4 archivos)
│   ├── ejemplo_area.py
│   ├── ejemplo_volumen.py
│   ├── ejemplo_longitud_arco.py
│   └── ejemplo_trabajo.py
├── datos/                       # Almacenamiento de datos
├── gui.py                       # 🆕 INTERFAZ GRÁFICA
├── menu.py                      # Menú interactivo
├── main.py                      # Punto de entrada
├── README.md                    # Este archivo
├── GUIA_USO.md                  # Guía completa (25 KB)
├── GUIA_GUI.md                  # Guía de interfaz gráfica
├── RESUMEN_PROYECTO.md          # Resumen ejecutivo
└── requirements.txt             # Dependencias
```

## 📦 Instalación

### Requisitos
- Python 3.8+
- pip (administrador de paquetes)

### Instalación de dependencias (ya incluida)
```bash
pip install numpy scipy matplotlib
```

Librerías instaladas:
- **numpy** - Cálculos numéricos
- **scipy** - Integración numérica avanzada
- **matplotlib** - Visualización de gráficos

## 📖 Documentación

### Para empezar:
1. **ESTE ARCHIVO** - Descripción general
2. **GUIA_GUI.md** - Cómo usar la interfaz gráfica ⭐ RECOMENDADO
3. **GUIA_USO.md** - Guía completa y técnica

### Contenido:
- Instrucciones de ejecución
- Descripción de módulos
- Ejemplos de código
- Consejos de aprendizaje
- Fórmulas matemáticas

## 🎓 Nivel Educativo
- **Curso**: Cálculo Integral
- **Nivel**: Intermedio (post-Cálculo I)
- **Duración**: 8-12 horas
- **Requisitos**: Cálculo Diferencial básico

## 💡 Casos de Uso

### Estudiantes:
- Aprender aplicaciones de integrales
- Verificar cálculos numéricos
- Visualizar conceptos matemáticos

### Docentes:
- Demostración de conceptos
- Material para clases prácticas
- Evaluación de estudiantes

### Profesionales:
- Referencia rápida de fórmulas
- Cálculos numéricos precisos
- Análisis de sistemas

## 🔗 Ejemplos Incluidos

| Ejemplo | Tema | Resultado |
|---------|------|-----------|
| Área bajo curva | ∫₀³ x² dx | 9.0 ✅ |
| Volumen de cono | Rotación de x/3 | π ≈ 3.14 ✅ |
| Perímetro de círculo | Paramétrica | 2π ≈ 6.28 ✅ |
| Trabajo variable | F(x)=2x+1 | 30 J ✅ |

## ✨ Características Especiales

✓ **Métodos Múltiples** - Compara diferentes técnicas
✓ **Verificación** - Comparación con valores exactos
✓ **Código Abierto** - Modifica y personaliza
✓ **Bien Documentado** - Código comentado y claro
✓ **Ejemplos Reales** - Aplicaciones del mundo real
✓ **Interfaz Amigable** - Fácil de usar para todos

## 🛠️ Autor
Desarrollado como proyecto educativo de Cálculo Integral
**Versión**: 1.0 - 17 de enero de 2026
**Estado**: ✅ COMPLETADO Y FUNCIONAL

## 📞 Soporte
- Revisa la documentación en los archivos .md
- Consulta los ejemplos en la carpeta ejemplos/
- Lee los comentarios en el código

## 🎉 ¡Listo para Usar!
**Comienza ejecutando**: `python gui.py`
