import os
import sys
import urllib.request
import zipfile
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PIP_DIR = os.path.join(BASE_DIR, "pip_installed")
MDL_DIR = os.path.join(BASE_DIR, "mdl")
TEMP_DIR = os.path.join(BASE_DIR, "temp_pip")

# 🧹 pulizia temp
def clear_temp():
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True)

# 📥 installa modulo da DromiPip
def pip_install(modulo):
    print(f"[DromiPip] Installazione modulo: {modulo}")
    os.makedirs(PIP_DIR, exist_ok=True)
    os.makedirs(MDL_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)

    zip_url = f"https://github.com/DeMENIGECO/DromiPip/raw/main/{modulo}.zip"
    zip_path = os.path.join(TEMP_DIR, f"{modulo}.zip")
    extract_path = os.path.join(TEMP_DIR, modulo)

    try:
        clear_temp()
        print("[DromiPip] Download modulo...")
        urllib.request.urlretrieve(zip_url, zip_path)

        print("[DromiPip] Estrazione...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        # se ZIP contiene una cartella interna
        contenuto = os.listdir(extract_path)
        if len(contenuto) == 1 and os.path.isdir(os.path.join(extract_path, contenuto[0])):
            modulo_path = os.path.join(extract_path, contenuto[0])
        else:
            modulo_path = extract_path

        # destinazioni
        dst_pip = os.path.join(PIP_DIR, modulo)
        dst_mdl = os.path.join(MDL_DIR, modulo)

        # sovrascrive se già esiste
        if os.path.exists(dst_pip):
            shutil.rmtree(dst_pip)
        if os.path.exists(dst_mdl):
            shutil.rmtree(dst_mdl)

        print("[DromiPip] Copia modulo...")
        shutil.copytree(modulo_path, dst_pip)
        shutil.copytree(modulo_path, dst_mdl)

        print(f"[DromiPip] ✅ Modulo '{modulo}' installato!")

    except urllib.error.HTTPError:
        print(f"[Errore] Modulo '{modulo}' non trovato nella repo!")
    except Exception as e:
        print(f"[Errore pip] {e}")

# 📋 lista moduli installati
def pip_list():
    if not os.path.exists(PIP_DIR):
        print("Nessun modulo installato.")
        return

    moduli = os.listdir(PIP_DIR)
    if not moduli:
        print("Nessun modulo installato.")
        return

    print("Moduli installati:")
    for m in moduli:
        print(f" - {m}")

# ❌ rimuove modulo
def pip_remove(modulo):
    dst_pip = os.path.join(PIP_DIR, modulo)
    dst_mdl = os.path.join(MDL_DIR, modulo)

    if os.path.exists(dst_pip):
        shutil.rmtree(dst_pip)
    if os.path.exists(dst_mdl):
        shutil.rmtree(dst_mdl)

    print(f"[DromiPip] ❌ Modulo '{modulo}' rimosso!")