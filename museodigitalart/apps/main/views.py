from django.shortcuts import render
import sqlite3

def home(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')  # Assicurati di specificare il percorso corretto al tuo database SQLite
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    codice = request.GET.get('codice', '')
    descrizione = request.GET.get('descrizione', '')
    numeroSale = request.GET.get('numeroSale', '')
    sort_by = request.GET.get('sort_by', 'codice')
    sort_order = request.GET.get('sort_order', 'asc')

    # Costruzione della query SQL con i filtri
    query = """
    SELECT codice, descrizione, numeroSale
    FROM TEMA
    WHERE 1=1
    """

    if codice:
        query += f" AND codice = '{codice}'"
    if descrizione:
        query += f" AND descrizione LIKE '%{descrizione}%'"

    # Ordinamento
    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {
        'temi': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'codice': codice,
        'descrizione': descrizione,
        'numeroSale': numeroSale
    }

    return render(request, 'main/home.html', context)
