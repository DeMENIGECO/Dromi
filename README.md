<div align="center">

<img width="100" height="100" alt="dromi-icon" src="https://github.com/user-attachments/assets/e7766418-7818-402f-81e7-8703cb08a264" />

# Dromi 1.1.0

[![Passing](https://img.shields.io/badge/Test-passati-green)](https://github.com/DeMENIGECO/Dromi/blob/main/.github/SIGNIFICATES.md?sect=Test-passati#test-passati)
[![Chat](https://img.shields.io/badge/GitHub%20Discussions-vai-006400)](https://github.com/DeMENIGECO/Dromi/discussions)

_Go to PC's Dromi!_

</div>

## Tabella dei contenuti

- [Cos'è Dromi?](#cosè-dromi)
- [🔥 Novità nella versione 1.1.0](#novità-nella-versione-110)
- [🔄 Visualizza i comandi](#visualizza-i-comandi)
- [Esempio di codice](#esempio-di-codice)
- [Andare nella REPL](#andare-nella-repl)
- [Eseguire file](#eseguire-file)
- [Pacchetti](#pacchetti)
  - [Installare](#installare)
    - [Sicurezza nelle installazioni di PIP](#sicurezza-nelle-installazioni-di-pip)
  - [Visualizzarli tutti](#visualizzarli-tutti)
  - [Disinstallare](#disinstallare)
  - [Usare i moduli installati](#usare-i-moduli-installati)
- [Moduli Preinstallati](#moduli-preinstallati)
- [Installa](#installa)
  - [Ultima versione](#ultima-versione)
  - [Oppure una versione specifica](#oppure-una-versione-specifica)
- [🆕 Gruppo ChatGPT](#gruppo-chatgpt)
- [Usare le Dromi Apps](#usare-le-dromi-apps)
  - [Dromi Docs](#dromi-docs)
  - [🆕 DFIE](#dfie)
- [Compatibilità Windows 10 e 11](#compatibilità-windows-10-e-11)
- [Versione non compilata](#versione-non-compilata)

---

## Cos'è Dromi?
Dromi è un linguaggio per creare interfacce grafiche in modo semplice e veloce.

---
## Novità nella versione 1.1.0

- 🔄 Migliorata la sicurezza di PIP  
- ⚙️ Ottimizzazioni generali  
- 🐞 Correzione di bug minori  

---

## Visualizza i comandi
Digita nel terminale:

```Bash
dromi.exe
```
e dovrebbe apparire una guida dei comandi

> [!TIP]
> - Se il comando `dromi.exe` non funziona, prova `dromi`.
> - Se `dromi` funziona, usalo al posto di `dromi.exe` in tutta la repository.
> - Se non funziona neanche `dromi`, prova a reinstallare Dromi o fai il prossimo suggerimento.
> - Prova a usare `dromi` e poi la versione installata, ad esempio per la 1.0.2 usa `dromi102` (Funziona negli installer della 1.0.2+)

---

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

---

## Andare nella REPL
Digitate nel terminale:
```Bash
dromi.exe --mdl repl
```

Per aprire la REPL.

---

## Eseguire file
Digiate nel terminale:
```Bash
dromi.exe nomefile.dr
```
---

## Pacchetti

### Installare
Digitate nel terminale:

```Bash
dromi.exe --mdl pip install nomepacchetto
```

#### Sicurezza nelle installazioni di PIP
Nella versione 1.1.0 è stata messa più sicurezza a PIP.
Quindi adesso le installazioni di PIP saranno più sicure e ci saranno meno rischi.

### Visualizzarli tutti

Digitate nel terminale:
```Bash
dromi.exe --mdl pip list
```
### Disinstallare

Digitate nel terminale::
```Bash
dromi.exe --mdl pip remove nomepachetto
```

### Usare i moduli installati

ad esempio abbiamo installato `windawk`:

```dromi
from mdl import windawk

windawk.windawk()
```

---

## Moduli Preinstallati

- windawk
- oTst

---

## Installa

### Ultima Versione
👉 [Scarica l'ultima versione - Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.1.0/dromi_installer_64bit_windows_1.1.0.exe)

### Oppure una versione specifica

| Versione | Installa       | Supporto |
|:--------:|:--------------:|:---------|
| 1.1.0    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.1.0/dromi_installer_64bit_windows_1.1.0.exe)| Supportata |
| 1.0.3    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.3/dromi_installer_64bit_windows_1.0.3.exe)| Supportata | 
| 1.0.2    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.2/dromi_installer_64bit_windows_1.0.2.exe)| Supportata |
| 1.0.1    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.1/dromi_installer_64bit_windows_1.0.1.exe)| Supportata |
| 1.0.0    | [Windows 64 Bit](https://github.com/DeMENIGECO/Dromi/releases/download/1.0.0/dromi_installer_64bit_windows_1.0.0.exe)| Supportata |

> [!WARNING]
> - In entrambi i casi, dopo l'installazione riavvia il terminale per aggiornare il PATH.
> - Infatti Windows per trovare Dromi e altri programmi usa la variabile utente `Path`

> [!TIP]
> Nella 1.0.2 Abbiamo messo i Dromi Docs.
> Per vederli, vai nel menu start, cerca nelle sezioni `Dromi 1.0.2 Docs`.
> Se installi più versioni, potrebbe esserci una cartella specifica "Dromi Docs" per racchiuderli. (Alcuni collegamenti potrebbero non avere l'icona)
> Nella 1.0.3 Abbiamo sostituito questi collegamenti on un'applicazione, di nome Dromi Docs, che trova i Docs di ogni versione da solo

---

## Gruppo ChatGPT
Partecipa per approfindimento, suggerimenti e altro:

👉 https://demenigeco.github.io/githubpages/r/chatgpt/group-69d14df0f5848199b6c6e78a2d5ee867.html

---

## Usare le Dromi Apps

### Dromi Docs
Andate nl menù start, digitate "Dromi Docs" e aprite l'app "Dromi Docs" (Quella con l'icona di Dromi)

Selezionate la versione desiderata per accedere ai Docs locali.

### DFIE

Apri il menu Start, digita `DFIE` e avvia l'app **DFIE** (quella con l'icona di Dromi).

Per iniziare, apri un file Dromi:
- Vai su `File → Apri`
- Seleziona il file desiderato

DFIE evidenzia automaticamente il codice con colori specifici:

| Colore | Significato |
|--------|------------|
| 🟢 Verde | Funzioni Dromi |
| 🔴 Rosso | Imports |
| 🟠 Arancione | Variabili |
| 🟠 Chiaro | Commenti |
| 🔵 Azzurro | Funzioni utente |
| 🔴 Rosso + sottolineato | Errori |

Questa evidenziazione aiuta a leggere meglio il codice e trovare errori più velocemente.

Quando hai finito:
- Vai su `File → Salva`
- Il file verrà aggiornato

---

## Compatibilità Windows 10 e 11
Dromi Supporta Windows 10 e Windows 11.
Per vedere le versioni supportate:

- [Versioni supportate di Windows 11](https://github.com/DeMENIGECO/Dromi/tree/main/.github/compatibility/win11.md)
- [Versioni supportate di Windows 10](https://github.com/DeMENIGECO/Dromi/tree/main/.github/compatibility/win10.md)

---
## Versione non compilata
Vai alla versione non compilata di Dromi nella cartella `not-compiled`:

👉 [Vai alla cartella](https://github.com/DeMENIGECO/Dromi/tree/main/not-compiled/)

---

<p align="center">
  <img width="100" height="100" alt="dromi-icon" src="https://github.com/user-attachments/assets/e7766418-7818-402f-81e7-8703cb08a264" /><br>
  <strong>Dromi Softwares</strong><br>
  <sub>© 2026 DomeniGeco. Tutti i diritti riservati.</sub>
</p>
