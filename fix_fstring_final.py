#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('gui_simplificada.py', 'r', encoding='utf-8') as f:
    content = f.read()

# PASO 1: Remover TODOS los f"" que empiezan con "╔", "║", "╚", "─", "═"
# Y convertirlos a strings simples
import re

# Patrón: f"...\n" 
# Reemplazar f"X" con "X" donde X es un carácter especial
conversiones = [
    (r'f"(╔[^"]*)"', r'"\1"'),
    (r'f"(║[^"]*)"', r'"\1"'),
    (r'f"(╚[^"]*)"', r'"\1"'),
    (r'f"(─[^"]*)"', r'"\1"'),
    (r'f"(═[^"]*)"', r'"\1"'),
    (r'f"(📋[^"]*)"', r'"\1"'),
    (r'f"(📐[^"]*)"', r'"\1"'),
    (r'f"(🔍[^"]*)"', r'"\1"'),
    (r'f"(📊[^"]*)"', r'"\1"'),
    (r'f"(✅[^"]*)"', r'"\1"'),
    (r'f"(🔄[^"]*)"', r'"\1"'),
]

for pattern, repl in conversiones:
    content = re.sub(pattern, repl, content)

with open('gui_simplificada.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Conversión completada")
