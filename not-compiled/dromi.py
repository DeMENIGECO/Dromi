import os
import sys
import shutil
from pip import pip_install, pip_list, pip_remove  # pip.py già creato
import graf_lib as dr  # libreria GUI basata su Tkinter
from repl import start_repl  # REPL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MDL_DIR = os.path.join(BASE_DIR, "mdl")

# Aggiunge tutte le cartelle dei moduli installati a sys.path
if os.path.exists(MDL_DIR):
    for modulo in os.listdir(MDL_DIR):
        modulo_path = os.path.join(MDL_DIR, modulo)
        if os.path.isdir(modulo_path) and modulo_path not in sys.path:
            sys.path.insert(0, modulo_path)

# -----------------------------------------------------
# 🧠 Aggiunge funzioni GUI al namespace globale
globals()['dr'] = dr
globals()['h1'] = dr.h1
globals()['h2'] = dr.h2
globals()['h3'] = dr.h3
globals()['h4'] = dr.h4
globals()['p'] = dr.p
globals()['button'] = dr.button
globals()['inputer'] = dr.inputer
globals()['clear'] = dr.clear
globals()['update'] = dr.update
globals()['set_window_size'] = dr.set_window_size
globals()['set_window_title'] = dr.set_window_title
globals()['run'] = dr.run

# -----------------------------------------------------
# 🧠 Funzione per aggiungere moduli installati al path
def add_modules_to_path():
    """Aggiunge tutte le cartelle dei moduli installati a sys.path"""
    if os.path.exists(MDL_DIR):
        for modulo in os.listdir(MDL_DIR):
            modulo_path = os.path.join(MDL_DIR, modulo)
            if os.path.isdir(modulo_path) and modulo_path not in sys.path:
                sys.path.insert(0, modulo_path)

# -----------------------------------------------------
# 🧠 Funzione per eseguire un file .dr
def esegui_file(percorso_file):
    if not os.path.exists(percorso_file):
        print(f"Errore: file '{percorso_file}' non trovato")
        return

    # Prima di eseguire un modulo .dr
    namespace = globals().copy()  # copia delle funzioni globali
    namespace.update({
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
    })

    with open(percorso_file, "r", encoding="utf-8") as f:
        codice = f.read()
    try:
        exec(codice, namespace)  # usa il namespace con funzioni GUI
    except Exception as e:
        print(f"Errore eseguendo file '{percorso_file}': {e}")

# -----------------------------------------------------
# 🧠 Importa modulo Dromi
def importa_modulo(nome):
    possibile = os.path.join(MDL_DIR, nome)
    if not os.path.exists(possibile):
        print(f"Errore: modulo '{nome}' non trovato")
        return

    main_file = os.path.join(possibile, "main.dr")
    index_file = os.path.join(possibile, "index.dr")

    if os.path.exists(main_file):
        esegui_file(main_file)
    elif os.path.exists(index_file):
        esegui_file(index_file)
    else:
        print(f"Errore: '{nome}' non ha main.dr o index.dr")
        

# -----------------------------------------------------
# 📌 Main CLI
if __name__ == "__main__":
    add_modules_to_path()

    if len(sys.argv) >= 3 and sys.argv[1] == "--mdl":

        # 👉 REPL (mettila SUBITO)
        if sys.argv[2] == "repl":
            start_repl()

        # 👉 PIP
        elif sys.argv[2] == "pip":
            if len(sys.argv) >= 5 and sys.argv[3] == "install":
                pip_install(sys.argv[4])
            elif len(sys.argv) >= 4 and sys.argv[3] == "list":
                pip_list()
            elif len(sys.argv) >= 5 and sys.argv[3] == "remove":
                pip_remove(sys.argv[4])
            else:
                print("Comandi pip disponibili:")
                print(" pip install nome_modulo")
                print(" pip list")
                print(" pip remove nome_modulo")

        else:
            print("Modulo non riconosciuto.")

    # 👉 FILE .dr (solo se NON è --mdl)
    elif len(sys.argv) >= 2:
        esegui_file(sys.argv[1])

    else:
        import commds