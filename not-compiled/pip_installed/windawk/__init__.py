import os
import sys

# Aggiungi la cartella principale al path (quella di dromi.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import graf_lib as dr  # importa direttamente graf_lib dal path principale

# Costruisci il namespace GUI
namespace = {
    'dr': dr,
    'h1': dr.h1,
    'h2': dr.h2,
    'h3': dr.h3,
    'h4': dr.h4,
    'p': dr.p,
    'button': dr.button,
    'inputer': dr.inputer,
    'clear': dr.clear,
    'update': dr.update,
    'set_window_size': dr.set_window_size,
    'set_window_title': dr.set_window_title,
    'run': dr.run,
}

# Esegui main.dr in questo namespace
percorso = os.path.join(os.path.dirname(__file__), "main.dr")
with open(percorso, "r", encoding="utf-8") as f:
    codice = f.read()
exec(codice, namespace)

# Esporta eventuali funzioni principali dal namespace
globals().update(namespace)
