# Dromi 1.0.0
_Go to PC's Dromi!_
## Esempio di codice
Ecco un esempio di codice:

```dromi
set_window_size(600,400)
set_window_title("Prova Interfaccia")
h1("Benvenuto in Dromi GUI")
h2("Test sottotitolo")
p("Questa è una label normale")
button("Cliccami")
dr.init()
```

## Eseguire files

Se avete la versione in .py, allora andate nella cartella di dromi nel terminale e digitate:
```Bash
python dromi.py nomefile.dr
```

ma in .exe:
```PowerShell
dromi.exe nomefile.dr
```

## Pacchetti

###### Installare
Se avete la versione in .py, allora andate nella cartella di dromi nel terminale e digitate:
```Bash
python dromi.py --mdl pip install nomepacchetto
```

ma in .exe:
```PowerShell
dromi.exe --mdl pip install nomepacchetto
```

###### Visualizzarli tutti
Se avete la versione in .py, allora andate nella cartella di dromi nel terminale e digitate:
```Bash
python dromi.py --mdl pip list
```

ma in .exe:
```PowerShell
dromi.exe --mdl pip list
```
###### Disintallare
Se avete la versione in .py, allora andate nella cartella di dromi nel terminale e digitate:
```Bash
python dromi.py --mdl pip remove nomepachetto
```

ma in .exe:
```PowerShell
dromi.exe --mdl pip remove nomepachetto
```

###### Usare i moduli installati

ad esempio abbiamo installato `windawk`:

```dromi
from mdl import windawk

windawk.windawk()
```

## Installa


| Versione | Installa        |
|:--------:|:---------------|
| 1.0.0    | Fra poco il link|
