# main/views.py

from django.shortcuts import render
import sqlite3

def sala(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')  # Assicurati di specificare il percorso corretto al tuo database SQLite
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    numero = request.GET.get('numero', '')
    nome = request.GET.get('nome', '')
    superficie = request.GET.get('superficie', '')
    numeroOpere = request.GET.get('numeroOpere', '')
    temaSala = request.GET.get('temaSala', '')
    descrizione = request.GET.get('descrizione', '')
    nomeopera = request.GET.get('nomeopera', '')
    sort_by = request.GET.get('sort_by', 'numero')
    sort_order = request.GET.get('sort_order', 'asc')

    # Costruzione della query SQL con i filtri
    query = """
    SELECT DISTINCT SALA.numero, SALA.nome, SALA.superficie, SALA.numeroOpere, SALA.temaSala, TEMA.descrizione
    FROM SALA
    LEFT JOIN TEMA ON SALA.temaSala = TEMA.codice
    WHERE 1=1
    """

    if numero:
        query += f" AND SALA.numero = '{numero}'"
    if nome:
        query += f" AND SALA.nome LIKE '%{nome}%'"
    if superficie:
        query += f" AND SALA.superficie LIKE '%{superficie}%'"
    if numeroOpere:
        query += f" AND SALA.numeroOpere LIKE '%{numeroOpere}%'"
    if temaSala:
        query += f" AND SALA.temaSala = '{temaSala}'"
    if descrizione:
        query += f" AND TEMA.descrizione LIKE '%{descrizione}%'"
    if nomeopera:
          query = """
                    SELECT DISTINCT SALA.numero, SALA.nome, SALA.superficie, SALA.numeroOpere, SALA.temaSala, TEMA.descrizione, OPERA.titolo AS nomeopera
                    FROM SALA
                    LEFT JOIN TEMA ON SALA.temaSala = TEMA.codice
                    LEFT JOIN OPERA ON OPERA.espostaInSala = SALA.numero
                    WHERE 1=1 AND OPERA.titolo LIKE '%{nomeopera}%'
                    """

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {
        'sale': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'numero': numero,
        'nome': nome,
        'superficie': superficie,
        'numeroOpere': numeroOpere,
        'temaSala': temaSala,
        'descrizione': descrizione,
        'nomeopera': nomeopera
    }

    return render(request, 'main/sala.html', context)
