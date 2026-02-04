# � CALCULADORA DE INTEGRALES - Desafíos Educativos

## 🚀 CÓMO EJECUTAR

### ✨ La forma más FÁCIL (Recomendado):
```
1. Busca el archivo: ejecutar.bat
2. Haz doble click
3. ¡Listo! La aplicación se abrirá automáticamente
```

### 📝 Alternativa por terminal:
```powershell
cd "E:\PROYECTO CALCULO INTEGRAL"
python gui_simplificada.py
```

---

## 🎯 FUNCIONALIDADES PRINCIPALES

### 📚 Calculadora de Integrales
- Calcula integrales definidas usando el método de trapecios
- Visualización gráfica de la función y el área bajo la curva
- Soporta múltiples tipos de funciones

### 🎮 Desafíos Educativos (NUEVO)
- **3 Niveles de Dificultad**: Fácil, Medio, Difícil
- **Preguntas de Opción Múltiple**: A, B, C, D
- **Sistema de Puntos**:
  - Fácil: +10 puntos
  - Medio: +25 puntos
  - Difícil: +50 puntos
- **Gráficos en Tiempo Real**: Visualización interactiva
- **Feedback Inmediato**: Respuestas correctas/incorrectas

### 🎨 Diseño Moderno
- **Colores Morado Pastel**: Tema elegante y profesional
- **Interfaz Responsiva**: Se adapta a diferentes tamaños
- **Scroll Interactivo**: Rueda del ratón para navegar

---

## 📋 REQUISITOS

- Python 3.7 o superior
- Bibliotecas (automáticamente instaladas):
  - numpy
  - scipy
  - matplotlib
  - tkinter (incluido con Python)

---

## 🎓 CÓMO USAR LA APLICACIÓN

### Para Cálculos Normales:
1. Selecciona una función matemática
2. Define los límites de integración (a, b)
3. El gráfico se mostrará automáticamente
4. Los resultados se actualizarán en tiempo real

### Para Jugar (Desafíos):
1. Haz clic en **"🎮 Desafíos Educativos"**
2. Elige un nivel de dificultad
3. Lee el problema integral
4. **Selecciona la respuesta correcta (A, B, C o D)**
5. Haz clic en **"✓ Verificar Respuesta"**
6. ¡Gana puntos si aciertas! ⭐

---

## 📁 ESTRUCTURA DEL PROYECTO

```
PROYECTO CALCULO INTEGRAL/
├── gui_simplificada.py      ← Archivo principal
├── src/                      ← Código de cálculos
│   ├── calculadora_integrales.py
│   ├── longitud_arco.py
│   ├── volumen_revolucion.py
│   ├── trabajo_energia.py
│   └── visualizador.py
├── .venv/                    ← Librerías (NO borrar)
├── requirements.txt          ← Dependencias
├── README.md                 ← Documentación
└── ejecutar.bat              ← Ejecutor (acceso directo)
```

---

## ✨ CARACTERÍSTICAS DESTACADAS

✅ **Múltiples Métodos de Integración**
- Método de Trapecios (por defecto)
- Cálculo de longitud de arco
- Volúmenes de revolución
- Trabajo y energía

✅ **Visualización Avanzada**
- Gráficos 2D de funciones
- Área sombreada bajo la curva
- Actualización en tiempo real
- Escalas automáticas

✅ **Modo Educativo Gamificado**
- Sistema de puntuación
- Niveles de dificultad progresivos
- Opciones múltiples aleatorias
- Pistas y retroalimentación instantánea

---

## 🆘 SOLUCIÓN DE PROBLEMAS

**P: ¿Qué hago si dice "Python no está instalado"?**
R: Descarga Python desde https://www.python.org/downloads/ e instálalo

**P: ¿La app se abre pero no carga?**
R: Asegúrate de que todas las librerías estén instaladas ejecutando:
```
pip install -r requirements.txt
```

**P: ¿Los gráficos no se muestran?**
R: Asegúrate de tener matplotlib instalado. Si no, ejecuta:
```
pip install matplotlib
```

---

## 👨‍💻 AUTOR

Calculadora de Integrales con Desafíos Educativos v2.0
Desarrollado con Python y tkinter

---

**¡Disfruta aprendiendo cálculo integral de forma interactiva! 🚀**- Feedback visual inmediato

### 📊 Gráficos Mejorados
- Colores pasteles en los gráficos
- Fondos personalizados por tema
- Grid suave y legible
- Leyendas elegantes

---

## 📁 ARCHIVOS NUEVOS:

```
✅ gui.py                 - Nueva versión moderna (ÚSALO)
✅ gui_antiguo.py        - Backup de versión anterior (si quieres volver)
✅ ejecutar_v25.bat      - Script para instalar + ejecutar (recomendado)
✅ instalar_v25.bat      - Solo instala dependencias
✅ verificar_instalacion.py - Verifica dependencias
✅ BIENVENIDA_V25.txt    - Mensaje de bienvenida
✅ README_V25.md         - Documentación completa
✅ COMPARATIVA_V25.md    - Comparación v2.0 vs v2.5
✅ INSTALACION_V25.md    - Guía paso a paso
✅ MODERNIZACION.md      - Resumen de cambios
```

---

## 💻 REQUISITOS:

- Python 3.9+
- Windows 7+, macOS, o Linux
- 512 MB RAM mínimo

---

## 📋 CHECKLIST:

- [x] CustomTkinter instalado ✅
- [x] Colores pasteles implementados ✅
- [x] Temas oscuro/claro funcionales ✅
- [x] Gráficos coloreados ✅
- [x] Animaciones implementadas ✅
- [x] Documentación completa ✅
- [x] Scripts de instalación listos ✅

---

## 🎯 CARACTERÍSTICAS:

### Calculadora de Integrales
- Método de Rectángulos
- Método de Trapecios
- Visualización en tiempo real

### Sustitución Trigonométrica
- Identidades automáticas
- Cálculo avanzado
- Procedimientos detallados

### Longitud de Arco
- Coordenadas cartesianas
- Parametrizaciones
- Precisión numérica

### Volumen de Revolución
- Método de discos
- Método de capas cilíndricas
- Visualización 3D

---

## 🔧 SOLUCIÓN RÁPIDA DE PROBLEMAS:

**Si algo no funciona:**

```powershell
# Verificar instalación
python verificar_instalacion.py

# Reinstalar CustomTkinter
pip install --upgrade customtkinter --force-reinstall

# Instalar todo de nuevo
pip install -r requirements.txt
```

---

## 📚 DOCUMENTACIÓN:

| Archivo | Para qué |
|---------|----------|
| `README_V25.md` | Guía completa de características |
| `COMPARATIVA_V25.md` | Ver diferencias v2.0 vs v2.5 |
| `INSTALACION_V25.md` | Instalación paso a paso |
| `MODERNIZACION.md` | Resumen de cambios |

---

## 🎁 BONUS:

✓ Versión anterior respaldada en `gui_antiguo.py`
✓ Puedes usar ambas versiones
✓ Código matemático 100% compatible
✓ Solo cambió la interfaz visual

---

## 💡 TIPS:

1. **Primera vez:** Usa `ejecutar_v25.bat` para instalar todo automáticamente
2. **Próximas veces:** Solo ejecuta `python gui.py`
3. **Cambiar tema:** Haz click en el botón 🌙 en el header
4. **Ver ejemplos:** Usa los botones de EJEMPLOS RÁPIDOS

---

## ¡LISTO! 🚀

Tu aplicación ahora es:
- ✨ **Moderna**
- 🎨 **Hermosa**
- 💻 **Profesional**
- 🚀 **Atractiva**

**Próximo paso:** Ejecuta `ejecutar_v25.bat` o `python gui.py`

---

Fecha: 26 de enero de 2026
Versión: 2.5
Estado: ✅ COMPLETADO
