1. Note Dromi Per Linux

Questo file racchiude alcune note su Dromi per Linux.

1.1. Moduli preinstallati mancanti

I moduli preinstallati sono mancanti nella build. 
Se avete aggiunto Dromi a una "variabile" per trovarlo del sistema, digiate nel terminale

dromi --mdl pip install windawk
dromi --mdl pip install oTst

Se non l'avete collegato a questa "variabile",
digiate nel terminale in cui avete estratto Dromi:

./dromi --mdl pip install windawk
./dromi --mdl pip install oTst

Così, potrete installarli.(1)

1.1.1. Come aggiungere la "variabile"

Per poter usare il comando dromi da qualsiasi terminale senza scrivere ./dromi, bisogna aggiungere la cartella di Dromi alla variabile di sistema PATH.

Prima trova dove si trova la cartella di Dromi (per esempio /home/utente/dromi).

Poi apri il file della tua shell:

- se usi bash: ~/.bashrc
- se usi zsh: ~/.zshrc

Aggiungi alla fine del file questa riga:

export PATH="$PATH:/home/utente/dromi"

Salva il file e ricaricalo con: 

source ~/.bashrc

Dopo questo, potrai usare semplicemente il comando dromi da qualsiasi terminale.

1.2. REPL Con Hardware sbagliato 

La REPL (La Dromi REPL) ha come hardware "Windows 64 Bit".
Perché noi distribuiamo i files non compilati al nostro Hardware Standard.

1.3. Build per linux non testata

La Build per Linux(2) non è stata testata.
Non significa che è instabile, ma non è stata testata umanamente.
Soltanto la build per Windows e i files .py sono testari.

2. Riflessioni

La Build per Linux(2) è una versione importante per Dromi in
modo da essere multi-sistema.

3. Note extra 

(1) = Sono solo i moduli preinstallati, e queste note non potrebbero essere aggiornate.
      Consultate il nostro README per la lista dei moduli predefiniti aggiornata.
(2) = Per "Build per Linux" si riferisce alla build per Linux e al Relativo contenuto.
