# Learn Dynamic Languages

Il repository contiene vari argomenti che permettono di spiegare cosa sono i linguaggi dinamici. In particolare verrà trattato il linguaggio dinamico per eccellenza, Python.

Il seguente repository e tutti i suoi file sono stati scritti di getto, flussi battuti direttamente sulla tastiera. Quindi è altamente probabile che siano presenti errori di battitura, grammaticali e costruzione di frasi.  
Piano piano, quando avrò voglia e tempo, proverò a rendere i concetti più semplici e chiari, oltre al correggere vari errori qua e là.

## Setup

Questo repository verrà redatto grazie a notebook python, ovvero file ipynb. I file IPython NoteBook permettono di scrivere testo in markdown, come questo, ma con l'aggiunta di sezione eseguibili grazie all'interprete IPython. Questo mi permette di eseguire esempi nello stesso file nel quale spiedo.

Detto ciò, per utilizzare file ipynb è necessario installare il package Jupyter.  
Quindi, creiamo un virtual environment appositamente per il corrente repository e successivamente installiamo jupyter.

```bash
python3 -m venv .env_ldl
source .env_ldl/bin/activate
(.env_ldl) pip install jupyter
```

Per utilizzare jupyter basta utilizzare il seguente comando dal virtual environment:

```bash
(.env_ldl) jupyter-notebook .
```

Dove il punto rappresenta la directory corrente, ma è possibile specificare un qualsiasi percorso assoluto o relativo.

Per concludere, una volta terminato l'utilizzo del virtual environment, si può uscire da esso con il comando

```bash
(.env_ldl) deactivate
```

## Argomenti trattati

Il repository tratterà i seguenti argomenti:

1. Linguaggio Python avanzato
    - Caratteristiche di base
    - Strutture dati e controllo
    - Classi e oggetti
    - Programmazione funzionale
    - Metaprogramming
    - Attributi e descrittori
2. Architettura di un interprete
    - Analisi lessicale, espressioni regolari e automi
    - Analisi sintattica, grammaticale
    - Gestione dei simboli e analisi semantica
    - Rappresentazione intermedia, AST e Bytecode
    - Disegno del frontend di un semplice linguaggio
3. Caratteristiche generali di un linguaggio dinamico
    - Tipizzazione
    - Gestione della memoria
    - Metaprogramming
    - Gestione degli errori
