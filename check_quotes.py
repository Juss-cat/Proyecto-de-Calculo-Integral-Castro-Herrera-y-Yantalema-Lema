#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('gui_simplificada.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Revisar líneas 480-492
for i in range(479, 492):
    line = lines[i].rstrip()
    # Contar f" y "
    f_count = line.count('f"')
    quote_count = line.count('"')
    print(f"Línea {i+1}: f\"={f_count}, \"={quote_count} | {line[:80]}")
