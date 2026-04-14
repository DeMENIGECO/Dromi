import tkinter as tk

class GrafLibRenderer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dromi App")
        self.window.geometry("800x600")
        self.widgets = []
        self.inputs = {}

    def set_size(self, w, h):
        self.window.geometry(f"{w}x{h}")

    def set_title(self, titolo):
        self.window.title(titolo)

    def h1(self, testo): self._add_label(testo, font=("Arial", 24, "bold"))
    def h2(self, testo): self._add_label(testo, font=("Arial", 20, "bold"))
    def h3(self, testo): self._add_label(testo, font=("Arial", 16, "bold"))
    def h4(self, testo): self._add_label(testo, font=("Arial", 14, "bold"))
    def p(self, testo): self._add_label(testo, font=("Arial", 12))
    
    def button(self, testo, command=None):
        btn = tk.Button(self.window, text=testo, command=command)
        btn.pack()
        self.widgets.append(btn)
        return btn

    def inputer(self, nome, default=""):
        var = tk.StringVar(value=default)
        entry = tk.Entry(self.window, textvariable=var)
        entry.pack()
        self.inputs[nome] = var
        self.widgets.append(entry)
        return var

    def _add_label(self, testo, font):
        lbl = tk.Label(self.window, text=testo, font=font)
        lbl.pack()
        self.widgets.append(lbl)
        return lbl

    def clear(self):
        for w in self.widgets:
            w.destroy()
        self.widgets.clear()
        self.inputs.clear()

    def update(self):
        self.window.update_idletasks()
        self.window.update()

    def run(self):
        self.window.mainloop()


# Singleton globale
_renderer = GrafLibRenderer()

# Funzioni esposte a Dromi
def h1(testo): return _renderer.h1(testo)
def h2(testo): return _renderer.h2(testo)
def h3(testo): return _renderer.h3(testo)
def h4(testo): return _renderer.h4(testo)
def p(testo): return _renderer.p(testo)
def button(testo, command=None): return _renderer.button(testo, command)
def inputer(nome, default=""): return _renderer.inputer(nome, default)
def clear(): return _renderer.clear()
def update(): return _renderer.update()
def set_window_size(w,h): return _renderer.set_size(w,h)
def set_window_title(titolo): return _renderer.set_title(titolo)
def run(): _renderer.window.mainloop()
def init(): _renderer.run()

# Singleton globale
_renderer = GrafLibRenderer()

# Esponiamo un oggetto 'window' dentro dr
window = _renderer.window

# Funzioni esposte
h1 = _renderer.h1
h2 = _renderer.h2
h3 = _renderer.h3
h4 = _renderer.h4
p = _renderer.p
button = _renderer.button
inputer = _renderer.inputer
clear = _renderer.clear
update = _renderer.update
set_window_size = _renderer.set_size
set_window_title = _renderer.set_title
run = _renderer.window.mainloop