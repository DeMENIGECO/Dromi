# Dromi 1.0.0
_Go to PC's Dromi!_

![Passing](https://img.shields.io/badge/Test-passati-green)
[![Chat](https://img.shields.io/badge/GitHub%20Discussions-vai-006400)](https://github.com/DeMENIGECO/Dromi/discussions)
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


| Versione | Installa        |
|:--------:|:---------------|
| 1.0.0    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.0/dromi_installer_64bit_windows_1.0.0.exe)|
