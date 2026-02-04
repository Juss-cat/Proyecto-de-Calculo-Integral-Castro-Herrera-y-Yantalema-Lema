#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('gui_simplificada.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'f"' in line and '{' in line and '\\n' in line:
        print(f"Línea {i}: {line.rstrip()}")
        # Mostrar solo las primeras 10
        if i > 600:
            break
