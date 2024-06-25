from django.shortcuts import render
import sqlite3
import random

def home(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Costruzione della query SQL per ottenere i dati dei temi
    tema_query = """
    SELECT TEMA.codice, TEMA.descrizione, TEMA.numeroSale
    FROM TEMA
    """
    
    cursor.execute(tema_query)
    temi = cursor.fetchall()

    # Costruzione della query SQL per ottenere i dati delle sale
    sala_query = """
    SELECT DISTINCT SALA.numero, SALA.nome, SALA.superficie, SALA.numeroOpere
    FROM SALA
    """
    
    cursor.execute(sala_query)
    sale = cursor.fetchall()

    # Costruzione della query SQL per ottenere i dati delle opere
    opera_query = """
    SELECT OPERA.opera, OPERA.autore, AUTORE.nome, AUTORE.cognome, OPERA.titolo,
           OPERA.annoAcquisto, OPERA.annoRealizzazione, OPERA.tipo, OPERA.espostaInSala
    FROM OPERA
    LEFT JOIN AUTORE ON OPERA.autore = AUTORE.codice
    JOIN SALA ON OPERA.espostaInSala = SALA.numero
    """
    
    cursor.execute(opera_query)
    opere = cursor.fetchall()

    autore_query = """
    SELECT AUTORE.codice, AUTORE.nome, AUTORE.cognome, AUTORE.nazione, 
           AUTORE.dataNascita, AUTORE.dataMorte, AUTORE.tipo, AUTORE.numeroOpere
    FROM AUTORE
    """

    
    cursor.execute(autore_query)
    autori = cursor.fetchall()

    cursor.close()
    conn.close()

    # Mescola i temi, le sale e le opere in modo casuale
    random.shuffle(temi)
    random.shuffle(sale)
    random.shuffle(opere)
    random.shuffle(autori)

    context = {
        'temihome': temi,
        'salahome': sale,
        'operahome': opere,
        'autorehome': autori
    }

    return render(request, 'main/home.html', context)
