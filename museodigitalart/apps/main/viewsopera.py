from django.shortcuts import render
import sqlite3

def opera(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    opera = request.GET.get('opera', '')
    autore = request.GET.get('autore', '')
    nome = request.GET.get('nome', '')
    cognome = request.GET.get('cognome', '')
    titolo = request.GET.get('titolo', '')
    annoAcquisto = request.GET.get('annoAcquisto', '')
    annoRealizzazione = request.GET.get('annoRealizzazione', '')
    tipo = request.GET.get('tipo', '')
    espostaInSala = request.GET.get('espostaInSala', '')
    sort_by = request.GET.get('sort_by', 'opera')
    sort_order = request.GET.get('sort_order', 'asc')

    # Costruzione della query SQL con i filtri
    query = """
    SELECT
    OPERA.opera as opera,
    OPERA.autore,
    AUTORE.nome,
    AUTORE.cognome,
    OPERA.titolo,
    OPERA.annoAcquisto,
    OPERA.annoRealizzazione,
    OPERA.tipo,
    OPERA.espostaInSala
    FROM
    OPERA
    LEFT JOIN
    AUTORE ON OPERA.autore = AUTORE.codice
    JOIN
    SALA ON OPERA.espostaInSala = SALA.numero
    WHERE
    1=1
    """

    if opera:
        query += f" AND OPERA.opera = '{opera}'"
    if autore:
        query += f" AND AUTORE.codice = '{autore}'"
    if nome:
        query += f" AND AUTORE.nome LIKE '%{nome}%'"
    if cognome:
        query += f" AND AUTORE.cognome LIKE '%{cognome}%'"
    if titolo:
        query += f" AND OPERA.titolo LIKE '%{titolo}%'"
    if annoAcquisto:
        query += f" AND OPERA.annoAcquisto LIKE '%{annoAcquisto}%'"
    if annoRealizzazione:
        query += f" AND OPERA.annoRealizzazione LIKE '%{annoRealizzazione}%'"
    if tipo:
        query += f" AND OPERA.tipo LIKE '%{tipo}%'"
    if espostaInSala:
        query += f" AND OPERA.espostaInSala = '{espostaInSala}'"

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {
        'opere': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'opera': opera,
        'autore': autore,
        'nome': nome,
        'cognome': cognome,
        'titolo': titolo,
        'annoAcquisto': annoAcquisto,
        'annoRealizzazione': annoRealizzazione,
        'tipo': tipo,
        'espostaInSala': espostaInSala
    }

    return render(request, 'main/opera.html', context)


def opere_sala(request, sala_numero):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    opera = request.GET.get('opera', '')
    autore = request.GET.get('autore', '')
    nome = request.GET.get('nome', '')
    cognome = request.GET.get('cognome', '')
    titolo = request.GET.get('titolo', '')
    annoAcquisto = request.GET.get('annoAcquisto', '')
    annoRealizzazione = request.GET.get('annoRealizzazione', '')
    tipo = request.GET.get('tipo', '')
    espostaInSala = sala_numero
    sort_by = request.GET.get('sort_by', 'opera')
    sort_order = request.GET.get('sort_order', 'asc')

    # Costruzione della query SQL con i filtri
    query = """
    SELECT
    OPERA.opera as opera,
    OPERA.autore,
    AUTORE.nome,
    AUTORE.cognome,
    OPERA.titolo,
    OPERA.annoAcquisto,
    OPERA.annoRealizzazione,
    OPERA.tipo,
    OPERA.espostaInSala
    FROM
    OPERA
    LEFT JOIN
    AUTORE ON OPERA.autore = AUTORE.codice
    WHERE
    OPERA.espostaInSala = ?
    """

    if opera:
        query += f" AND OPERA.opera = '{opera}'"
    if autore:
        query += f" AND AUTORE.codice = '{autore}'"
    if nome:
        query += f" AND AUTORE.nome LIKE '%{nome}%'"
    if cognome:
        query += f" AND AUTORE.cognome LIKE '%{cognome}%'"
    if titolo:
        query += f" AND OPERA.titolo LIKE '%{titolo}%'"
    if annoAcquisto:
        query += f" AND OPERA.annoAcquisto LIKE '%{annoAcquisto}%'"
    if annoRealizzazione:
        query += f" AND OPERA.annoRealizzazione LIKE '%{annoRealizzazione}%'"
    if tipo:
        query += f" AND OPERA.tipo LIKE '%{tipo}%'"

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query, (sala_numero,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {
        'opere': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'opera': opera,
        'autore': autore,
        'nome': nome,
        'cognome': cognome,
        'titolo': titolo,
        'annoAcquisto': annoAcquisto,
        'annoRealizzazione': annoRealizzazione,
        'tipo': tipo,
        'espostaInSala': espostaInSala
    }

    return render(request, 'main/opera.html', context)


def opere_autore(request, autore_id):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    opera = request.GET.get('opera', '')
    nome = request.GET.get('nome', '')
    cognome = request.GET.get('cognome', '')
    titolo = request.GET.get('titolo', '')
    annoAcquisto = request.GET.get('annoAcquisto', '')
    annoRealizzazione = request.GET.get('annoRealizzazione', '')
    tipo = request.GET.get('tipo', '')
    espostaInSala = request.GET.get('espostaInSala', '')
    sort_by = request.GET.get('sort_by', 'opera')
    sort_order = request.GET.get('sort_order', 'asc')

    # Costruzione della query SQL con i filtri
    query = """
    SELECT
    OPERA.opera as opera,
    OPERA.autore,
    AUTORE.nome,
    AUTORE.cognome,
    OPERA.titolo,
    OPERA.annoAcquisto,
    OPERA.annoRealizzazione,
    OPERA.tipo,
    OPERA.espostaInSala
    FROM
    OPERA
    LEFT JOIN
    AUTORE ON OPERA.autore = AUTORE.codice
    WHERE
    OPERA.autore = ?
    """

    if opera:
        query += f" AND OPERA.opera = '{opera}'"
    if nome:
        query += f" AND AUTORE.nome LIKE '%{nome}%'"
    if cognome:
        query += f" AND AUTORE.cognome LIKE '%{cognome}%'"
    if titolo:
        query += f" AND OPERA.titolo LIKE '%{titolo}%'"
    if annoAcquisto:
        query += f" AND OPERA.annoAcquisto LIKE '%{annoAcquisto}%'"
    if annoRealizzazione:
        query += f" AND OPERA.annoRealizzazione LIKE '%{annoRealizzazione}%'"
    if tipo:
        query += f" AND OPERA.tipo LIKE '%{tipo}%'"
    if espostaInSala:
        query += f" AND OPERA.espostaInSala = '{espostaInSala}'"

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query, (autore_id,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {
        'opere': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'opera': opera,
        'nome': nome,
        'cognome': cognome,
        'titolo': titolo,
        'annoAcquisto': annoAcquisto,
        'annoRealizzazione': annoRealizzazione,
        'tipo': tipo,
        'espostaInSala': espostaInSala
    }

    return render(request, 'main/opera.html', context)