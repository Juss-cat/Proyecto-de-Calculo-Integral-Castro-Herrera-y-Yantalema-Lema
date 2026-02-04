#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('gui_simplificada.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar TODAS las instancias problemáticas
content = content.replace('f"─" * 56 + "\\n"', '"─" * 56 + "\\n"')
content = content.replace('f"═" * 56 + "\\n"', '"═" * 56 + "\\n"')
# También los casos de solo el patrón sin +
content = content.replace('f"─" * 56', '"─" * 56')
content = content.replace('f"═" * 56', '"═" * 56')

with open('gui_simplificada.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Reemplazo completado")

