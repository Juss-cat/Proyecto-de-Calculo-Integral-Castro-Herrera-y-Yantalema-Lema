#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('gui_simplificada.py', 'r', encoding='utf-8') as f:
    content = f.read()

# REEMPLAZOS SIMPLES Y DIRECTOS - sin regex
replacements = [
    ('f"╔════════════════════════════════════════════════════════╗\\n"', '"╔════════════════════════════════════════════════════════╗\\n"'),
    ('f"║         CÁLCULO DE INTEGRAL DEFINIDA                   ║\\n"', '"║         CÁLCULO DE INTEGRAL DEFINIDA                   ║\\n"'),
    ('f"║      INTEGRACIÓN POR SUSTITUCIÓN TRIGONOMÉTRICA        ║\\n"', '"║      INTEGRACIÓN POR SUSTITUCIÓN TRIGONOMÉTRICA        ║\\n"'),
    ('f"║              CÁLCULO DE LONGITUD DE ARCO               ║\\n"', '"║              CÁLCULO DE LONGITUD DE ARCO               ║\\n"'),
    ('f"║       CÁLCULO DE VOLUMEN DE SÓLIDO DE REVOLUCIÓN       ║\\n"', '"║       CÁLCULO DE VOLUMEN DE SÓLIDO DE REVOLUCIÓN       ║\\n"'),
    ('f"╚════════════════════════════════════════════════════════╝\\n\\n"', '"╚════════════════════════════════════════════════════════╝\\n\\n"'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('gui_simplificada.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Reemplazo nuclear completado")
