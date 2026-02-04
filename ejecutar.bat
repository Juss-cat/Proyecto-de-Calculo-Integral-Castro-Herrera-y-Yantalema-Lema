@echo off
chcp 65001 > nul
color 0D
cls

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                     🎮 CALCULADORA DE INTEGRALES                       ║
echo ║                        Desafíos Educativos                             ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.
echo 📚 Iniciando aplicación...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado o no está en el PATH
    echo.
    echo Por favor instala Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Cambiar a directorio del proyecto
cd /d "%~dp0"

REM Activar ambiente virtual
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else (
    echo ⚠️  Ambiente virtual no encontrado. Creando...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    echo 📦 Instalando dependencias...
    pip install -q -r requirements.txt
)

REM Ejecutar la aplicación
python gui_simplificada.py

REM Si la app se cierra, mostrar mensaje
if errorlevel 1 (
    echo.
    echo ❌ Error al ejecutar la aplicación
    pause
) else (
    echo.
    echo ✅ Aplicación cerrada correctamente
)

pause
