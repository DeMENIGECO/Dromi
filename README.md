# Dromi 1.0.1
[![Passing](https://img.shields.io/badge/Test-passati-green)](https://github.com/DeMENIGECO/Dromi/blob/main/.github/SIGNIFICATES.md?sect=significato-badge-test-passati#significato-badge-test-passati)
[![Chat](https://img.shields.io/badge/GitHub%20Discussions-vai-006400)](https://github.com/DeMENIGECO/Dromi/discussions)

_Go to PC's Dromi!_


## Visualizza i comandi
Digita nel terminale:

```Bash
dromi.exe
```
e dovrebbe apparire:

```Output
Uso:
 dromi.exe file.dr
 dromi.exe --mdl pip install nome_modulo
 dromi.exe --mdl pip list
 dromi.exe --mdl pip remove nome_modulo

Esempi:
 dromi.exe example.dr
 dromi.exe --mdl pip install windawk
```

> [!TIP]
> - Se il comando "dromi.exe" non funziona, prova "dromi".
> - Se "dromi" funziona, usalo al posto di "dromi.exe" in tutta la repository.
> - Se non funziona neanche "dromi", prova a reinstallare Dromi.

## Esempio di codice
Ecco un esempio di codice: (fai un file `test.dr`)

```dromi
set_window_size(600,400)
set_window_title("Prova Interfaccia")
h1("Benvenuto in Dromi GUI")
h2("Test sottotitolo")
p("Questa è una label normale")
button("Cliccami")
dr.init()
```

poi nel terminale digita:

```Bash
dromi.exe test.dr
```

## Andare nella REPL
Digitate nel terminale:
```Bash
dromi.exe --mdl repl
```

Per aprire la REPL.

## Eseguire file
Digiate nel terminale:
```Bash
dromi.exe nomefile.dr
```

## Pacchetti

###### Installare
Digitate nel terminale:

```Bash
dromi.exe --mdl pip install nomepacchetto
```

###### Visualizzarli tutti

Digitate nel terminale:
```Bash
dromi.exe --mdl pip list
```
###### Disintallare

Digitate nel terminale::
```Bash
dromi.exe --mdl pip remove nomepachetto
```

###### Usare i moduli installati

ad esempio abbiamo installato `windawk`:

```dromi
from mdl import windawk

windawk.windawk()
```
## Moduli Preinstalalti

- windawk
- oTst

## Installa


| Versione | Installa       | Supporto |
|:--------:|:--------------:|:---------|
| 1.0.1    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.1/dromi_installer_64bit_windows_1.0.1.exe)| Supportata |
| 1.0.0    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.0/dromi_installer_64bit_windows_1.0.0.exe)| Supportata |

---

<p align="center">
  <img width="100" height="100" alt="dromi-icon" src="https://github.com/user-attachments/assets/e7766418-7818-402f-81e7-8703cb08a264" /><br>
  <strong>Dromi Softwares</strong><br>
  <sub>© 2026 DomeniGeco. Tutti i diritti riservati.</sub>
</p>
