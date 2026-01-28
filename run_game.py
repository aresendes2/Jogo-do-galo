#!/usr/bin/env python3
"""
Script de lançamento que detecta automaticamente o Python correto.
Tenta usar /usr/local/bin/python3 primeiro (que tem Tkinter funcional),
e se não existir, usa o python3 do PATH.
"""

import sys
import subprocess
from pathlib import Path

# Caminho do ficheiro main.py
SCRIPT_DIR = Path(__file__).resolve().parent
MAIN_PY = SCRIPT_DIR / "main.py"

# Tentar usar o Python de /usr/local/bin primeiro
PREFERRED_PYTHON = Path("/usr/local/bin/python3")

if PREFERRED_PYTHON.exists():
    python_exe = str(PREFERRED_PYTHON)
else:
    python_exe = sys.executable

# Executar o main.py com o Python correto
try:
    subprocess.run([python_exe, str(MAIN_PY)], check=True)
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar o jogo: {e}", file=sys.stderr)
    sys.exit(1)
except KeyboardInterrupt:
    print("\nJogo interrompido pelo utilizador.")
    sys.exit(0)
