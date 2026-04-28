import sys
import graf_lib as dr  # libreria GUI basata su Tkinter

def start_repl():
    print("Dromi 1.1.1 - Windows 64 Bit")
    print("Scrivi 'exit' per uscire\n")

    # Ambiente globale condiviso (importantissimo)
    namespace = globals().copy()
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

    while True:
        try:
            code = input(">>> ")

            # uscita
            if code.strip() in ["exit", "quit"]:
                print("Uscita dalla REPL.")
                break

            if not code.strip():
                continue

            # supporto multilinea semplice
            if code.endswith(":"):
                lines = [code]
                while True:
                    next_line = input("... ")
                    if next_line.strip() == "":
                        break
                    lines.append(next_line)
                code = "\n".join(lines)

            # esecuzione codice Dromi
            exec(code, namespace)

        except Exception as e:
            print(f"[Errore] {e}")