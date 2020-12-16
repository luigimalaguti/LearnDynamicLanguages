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

1. [Linguaggio Python avanzato](1_LinguaggioPython/README.md)
    - [Caratteristiche di base](1_LinguaggioPython/1_Caratteristiche_di_base.ipynb)
    - [Strutture dati e controllo](1_LinguaggioPython/2_Strutture_dati_e_controllo.ipynb)
    - [Classi e oggetti](1_LinguaggioPython/3_Classi_e_oggetti.ipynb)
    - [Attributi e descrittori](1_LinguaggioPython/4_Attributi_e_descrittori.ipynb)
    - [Creazione degli oggetti](1_LinguaggioPython/5_Creazione_degli_oggetti.ipynb)
    - Metaprogramming
    - Programmazione funzionale
    - Complementi sugli oggetti
2. [Architettura di un interprete](2_Architettura/README.md)
    - [Compilatori e interpreti](2_Architettura/1_Compilatori_e_interpreti.ipynb)
    - [Analisi lessicale, espressioni regolari](2_Architettura/2_Analisi_lessicale.ipynb)
    - [Analisi sintattica, grammatiche](2_Architettura/3_Analisi_sintattica.ipynb)
    - [Rappresentazione intermedia, AST e Bytecode](2_Architettura/4_Rappresentazione_intermedia.ipynb)
    - [Il linguaggio PERL](5_PERL.ipynb)
3. [Caratteristiche generali di un linguaggio dinamico](3_LinguaggioDinamico/README.md)
    - Tipizzazione
    - Gestione della memoria
    - Metaprogramming
    - Gestione degli errori

## Suggerimento ordine degli argomenti

Personalmente ho seguito il corso di Linguaggi Dinamici affrontando gli argomenti nel seguente ordine:

1. [Linguaggio Python avanzato](1_LinguaggioPython/README.md)
    - [Caratteristiche di base](1_LinguaggioPython/1_Caratteristiche_di_base.ipynb)
    - [Strutture dati e controllo](1_LinguaggioPython/2_Strutture_dati_e_controllo.ipynb)
    - [Classi e oggetti](1_LinguaggioPython/3_Classi_e_oggetti.ipynb)
2. [Architettura di un interprete](2_Architettura/README.md)
    - [Compilatori e interpreti](2_Architettura#1_Compilatori_e_interpreti.ipynb)
    - [Analisi lessicale, espressioni regolari](2_Architettura/2_Analisi_lessicale.ipynb)
    - [Analisi sintattica, grammatiche](2_Architettura/3_Analisi_sintattica.ipynb)
    - [Rappresentazione intermedia, AST e Bytecode](2_Architettura/4_Rappresentazione_intermedia.ipynb)
    - [Il linguaggio PERL](5_PERL.ipynb)
3. [Linguaggio Python avanzato](1_LinguaggioPython/README.md)
    - [Attributi e descrittori](1_LinguaggioPython/4_Attributi_e_descrittori.ipynb)
    - [Creazione degli oggetti](1_LinguaggioPython/5_Creazione_degli_oggetti.ipynb)
    - Metaprogramming
4. [Caratteristiche generali di un linguaggio dinamico](3_LinguaggioDinamico/README.md)
    - Tipizzazione
    - Gestione della memoria
    - Metaprogramming
    - Gestione degli errori
5. [Linguaggio Python avanzato](1_LinguaggioPython/README.md)
    - Programmazione funzionale
    - Complementi sugli oggetti
