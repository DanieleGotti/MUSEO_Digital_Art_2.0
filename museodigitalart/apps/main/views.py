from django.shortcuts import render
import sqlite3
import random  # Importa il modulo random

def temahome(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Costruzione della query SQL senza filtri
    query = """
    SELECT TEMA.codice, TEMA.descrizione, TEMA.numeroSale
    FROM TEMA
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Debugging: Stampa i dati nella console
    print("Temi:", rows)  # Stampa i dati nella console del server

    # Mescola i temi in modo casuale
    random.shuffle(rows)

    context = {
        'temihome': rows
    }

    return render(request, 'main/home.html', context)
