from django.shortcuts import render
import sqlite3
import random  # Importa il modulo random

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

    cursor.close()
    conn.close()

    # Debugging: Stampa i dati nella console
    print("Temi:", temi)  # Stampa i dati dei temi nella console del server
    print("Sale:", sale)  # Stampa i dati delle sale nella console del server

    # Mescola i temi e le sale in modo casuale
    random.shuffle(temi)
    random.shuffle(sale)

    context = {
        'temihome': temi,
        'salahome': sale
    }

    return render(request, 'main/home.html', context)
