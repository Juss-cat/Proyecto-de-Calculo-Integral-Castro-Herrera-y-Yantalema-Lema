#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

with open('gui_simplificada.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Buscar patrones f"... (con caracteres especiales) ... " * NUM  
    # y reemplazarlos sin el f
    if re.search(r'f"[─═]" \* \d+', line):
        line = re.sub(r'f"([─═])" ', r'"\1" ', line)
    new_lines.append(line)

with open('gui_simplificada.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✓ Limpieza completada")
