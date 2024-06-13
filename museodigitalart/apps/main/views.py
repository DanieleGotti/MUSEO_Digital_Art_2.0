from django.shortcuts import render
import sqlite3

# Create your views here.

from .models import Tema

def home(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')  # Assicurati di specificare il percorso corretto al tuo database SQLite

    # Creazione di un cursore per eseguire query SQL
    cursor = conn.cursor()

    # Query per selezionare tutti gli elementi dalla tabella TEMA
    query = "SELECT * FROM TEMA"

    # Esecuzione della query
    cursor.execute(query)

    # Recupero di tutti i risultati
    rows = cursor.fetchall()

    # Chiusura del cursore e della connessione al database
    cursor.close()
    conn.close()

    # Preparazione dei dati da passare al template HTML
    context = {
        'temi': rows  # Passiamo i risultati della query come contesto al template
    }

    # Renderizza il template HTML e passa il contesto
    return render(request, 'main/home.html', context)

