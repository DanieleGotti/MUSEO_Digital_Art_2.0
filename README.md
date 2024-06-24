# Progetto 2 Programmazione Web 23/24
Versione 2.0
![logo](https://github.com/DanieleGotti/MUSEO_Digital_Art/blob/main/img/logos/logo.png)

[Museo - Digital Art_2.0](https://museodigitalart.altervista.orgAAAAA) è un sito web per la visualizzazione di temi, sale, opere e autori di un museo.
Questo progetto è stato realizzato ristrutturando il precedente [Museo - Digital_Art](https://museodigitalart.altervista.org) ([Git](https://github.com/DanieleGotti/MUSEO_Digital_Art.git)) con liguaggio python e l'utilizzo dei framework [Django](https://www.djangoproject.com/) e [Bootstrap](https://getbootstrap.com/).


## Installazione del software e procedura per l'avvio
Quando abbiamo finito facciamo delle prove e completiamo questa sezione

## Database

Il Database utilizzato per questo progetto è lo stesso impiegato nel progetto precedente, esportato da Altervista in SQL e poi importato tramite query in SQLiteStudio. In questo ambiente, il nostro database è un file `.sqlite3`. Abbiamo optato per questa soluzione poiché è quella di default di Django. Infatti, nella modalità base, Django gestisce le sessioni tramite un database gestito da SQLite.

### Perché SQLite?

SQLite è un DBMS relazionale che è noto per essere leggero e facile da usare. Alcuni dei motivi per cui abbiamo scelto SQLite includono:

- **Facilità d'uso**: SQLite non richiede un server separato per operare, il che semplifica l'installazione e la configurazione. È sufficiente avere il file `.sqlite3` nel progetto.
- **Portabilità**: Il database è memorizzato in un singolo file, il che rende facile il trasferimento e la condivisione tra diversi ambienti di sviluppo.
- **Prestazioni**: Per progetti di piccola e media scala, SQLite offre prestazioni adeguate senza la complessità di un DBMS più grande.
- **Compatibilità con Django**: SQLite è supportato nativamente da Django, rendendo l'integrazione semplice e senza problemi.

### Integrazione con Django

Django utilizza il file di configurazione `settings.py` per definire quale database utilizzare. 


## Django

Il progetto Django si basa sul pattern MVC (Model-View-Controller):

- **Model**: Rappresenta il database, contenente i dati.
- **View**: I file `.html` all'interno della directory `templates`, responsabili dell'interfaccia utente.
- **Controller**: I file `.py` denominati `views`, che gestiscono i dati in risposta all'interazione dell'utente con la view.

Inizialmente, il progetto è composto da due directory principali: `database` (contenente il DB) e `museodigitalart`. All'interno di `museodigitalart` troviamo:

### 1. templates
Questa directory contiene i file HTML che gestiscono la visualizzazione delle varie pagine del sito. I componenti principali includono:

- **footer.html**: La sezione del footer del sito.
- **header.html**: La sezione dell'header del sito.
- **nav.html**: La barra di navigazione del sito.

### 2. static
Questa cartella contiene i file statici utilizzati dall'applicazione, organizzati in sottodirectory:

- **js**: File JavaScript.
- **img**: File immagine.
- **css**: Fogli di stile.

### 3. apps
All'interno della directory `apps` troviamo la cartella `main`, che è cruciale per l'applicazione:

- **templates/main**: I template HTML per le diverse pagine.
- **views.py**: File Python che gestiscono la logica e la gestione dei dati.
- **settings.py**: Configurazioni dell'applicazione.
- **urls.py**: Gestione delle URL e del routing dell'applicazione.

### 4. museodigitalart
Questa directory contiene i file di configurazione principali:

- **settings.py**: Il file di configurazione principale del progetto.
- **urls.py**: Il file principale per la configurazione delle URL, che rimanda a `urls.py` nella cartella `main` all'interno di `apps`.

Questa struttura consente una chiara separazione delle responsabilità, rendendo il progetto più facile da gestire e scalare.


## Struttura

#### Home 
Se teniamo le card possiamo anche eliminare questo pezzo, se mettiamo altro spieghiamo quello

#### Temi, Sale, Opere, Autori
La grafica dei templates è stata modificata, considerando che l'uso di Bootstrap rende il sito già reattivo. Di conseguenza, abbiamo rimosso il pulsante accanto ai filtri. Per il resto, abbiamo cercato di ricreare fedelmente la grafica del primo progetto, ma utilizzando Bootstrap.

Tuttavia, la barra di navigazione, essendo molto personalizzata, è stata mantenuta identica tramite l'uso esclusivo di CSS.


#### Gestione Autori (CRUD)
Il sistema CRUD è stato sviluppato in modo coerente con il primo progetto, cercando di ricreare la stessa grafica per le diverse funzioni. Sono stati utilizzati modali per gestire l'inserimento e le conferme, sostituendo i popup e gli alert precedentemente impiegati per le conferme delle azioni. 

All'interno dei form di inserimento e di modifica, è stato sfruttato Bootstrap, utilizzando le funzioni di datepicker per le date e un menu a tendina per la selezione della nazione. La scelta di non includere il menu a tendina nel form di modifica è stata voluta, in quanto potrebbe essere necessario modificare una nazione non trovata tramite il menu a tendina.

Come nel progetto precedente, nel form di modifica non è possibile modificare il codice e il tipo, che vengono calcolati automaticamente in base alla modifica o meno della data di morte.

Il form di inserimento presenta diversi controlli che mostrano eventuali problemi immediatamente (se non vengono compilati tutti i campi) o successivamente, sfruttando la funzione `messages` di Django. Il messaggio relativo all'operazione verrà mostrato in alto, sotto l'header, con colori diversi a seconda dell'esito dell'azione stessa.



### GUI

L'utilizzo di Bootstrap ha permesso di velocizzare lo sviluppo della GUI, risparmiando tempo e riducendo la quantità di codice CSS necessario. Abbiamo cercato di riprodurre il più fedelmente possibile l'interfaccia originale, riutilizzando le parti migliori del progetto precedente. Tuttavia, abbiamo anche introdotto alcune differenze per mettere in mostra le potenzialità di Bootstrap e per migliorare l'aspetto generale dell'interfaccia.

Bootstrap ci ha offerto numerosi vantaggi, tra cui:

- **Reattività**: Il sito è automaticamente ottimizzato per diverse dimensioni di schermo senza bisogno di ulteriori interventi CSS.
- **Consistenza**: L'uso di componenti predefiniti ha garantito un aspetto uniforme e professionale in tutte le pagine.
- **Velocità di sviluppo**: Grazie alle classi predefinite di Bootstrap, abbiamo potuto implementare rapidamente layout complessi e funzionalità avanzate.

Abbiamo sfruttato componenti specifici di Bootstrap, come il **datepicker** per la selezione delle date e i **menu a tendina** per la scelta di opzioni predefinite, rendendo l'interfaccia più intuitiva e user-friendly.

Nonostante l'adozione di Bootstrap, abbiamo mantenuto alcune parti altamente personalizzate dell'interfaccia, come la barra di navigazione, utilizzando solo CSS per preservare il design originale. In questo modo, siamo riusciti a combinare il meglio del vecchio progetto con le nuove potenzialità offerte da Bootstrap.

## Gruppo
Nome gruppo: __DgFg24__ \
Componenti:
- [__Gotti Daniele, matricola 1079011__](https://github.com/DanieleGotti)
- [__Gervasoni Federica, matricola 1078966__](https://github.com/fgervasoni7)


