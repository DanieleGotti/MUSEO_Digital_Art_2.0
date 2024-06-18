from django.shortcuts import render, redirect
from django.db import connection

def get_connection():
    return connection  # Usa il connection object fornito da Django

def autore(request):
    conn = get_connection()
    cursor = conn.cursor()

    codice = request.GET.get('codice', '')
    nome = request.GET.get('nome', '')
    cognome = request.GET.get('cognome', '')
    nazione = request.GET.get('nazione', '')
    dataNascita = request.GET.get('dataNascita', '')
    dataMorte = request.GET.get('dataMorte', '')
    tipo = request.GET.get('tipo', '')
    numeroOpere = request.GET.get('numeroOpere', '')
    nomeopera = request.GET.get('nomeopera', '')
    sort_by = request.GET.get('sort_by', 'codice')
    sort_order = request.GET.get('sort_order', 'asc')

    mostra = False

    if request.method == 'POST' and 'toggle_crud' in request.POST:
        mostra = True

    query = get_autore_query(codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere, nomeopera, sort_by, sort_order)
    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    context = {
        'autori': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'codice': codice,
        'nome': nome,
        'cognome': cognome,
        'nazione': nazione,
        'dataNascita': dataNascita,
        'dataMorte': dataMorte,
        'tipo': tipo,
        'numeroOpere': numeroOpere,
        'nomeopera': nomeopera,
        'mostra': mostra,
    }

    return render(request, 'main/autore.html', context)

def get_autore_query(codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere, nomeopera, sort_by, sort_order):
    query = """
    SELECT AUTORE.codice, AUTORE.nome, AUTORE.cognome, AUTORE.nazione, AUTORE.dataNascita, AUTORE.dataMorte, AUTORE.tipo, AUTORE.numeroOpere
    FROM AUTORE
    WHERE 1=1
    """

    if codice:
        query += f" AND AUTORE.codice = '{codice}'"
    if nome:
        query += f" AND AUTORE.nome LIKE '%{nome}%'"
    if cognome:
        query += f" AND AUTORE.cognome LIKE '%{cognome}%'"
    if nazione:
        query += f" AND AUTORE.nazione LIKE '%{nazione}%'"
    if dataNascita:
        query += f" AND AUTORE.dataNascita LIKE '%{dataNascita}%'"
    if dataMorte:
        query += f" AND AUTORE.dataMorte LIKE '%{dataMorte}%'"
    if tipo:
        query += f" AND AUTORE.tipo LIKE '%{tipo}%'"
    if numeroOpere:
        query += f" AND AUTORE.numeroOpere = {numeroOpere}"
    if nomeopera:
        query = f"""
        SELECT DISTINCT AUTORE.codice, AUTORE.nome, AUTORE.cognome, AUTORE.nazione, AUTORE.dataNascita, AUTORE.dataMorte, AUTORE.tipo, AUTORE.numeroOpere, OPERA.titolo AS nomeopera
        FROM AUTORE
        JOIN OPERA ON OPERA.autore = AUTORE.codice
        WHERE OPERA.titolo LIKE '%{nomeopera}%'
        """

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    return query

def create_autore(request):
    if request.method == 'POST':
        codice = request.POST['codice']
        nome = request.POST['nome']
        cognome = request.POST['cognome']
        nazione = request.POST['nazione']
        dataNascita = request.POST['dataNascita']
        dataMorte = request.POST.get('dataMorte', None)  # dataMorte è opzionale
        tipo = request.POST['tipo']
        numeroOpere = request.POST.get('numeroOpere', '0')  # default to '0' if not provided

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO AUTORE (codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('autore')

    return render(request, 'main/autore.html')

def update_autore(request, codice):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nome = request.POST['editNome']
        cognome = request.POST['editCognome']
        nazione = request.POST['editNazione']
        dataNascita = request.POST['editDataNascita']
        dataMorte = request.POST['editDataMorte']
        tipo = request.POST['editTipo']
        numeroOpere = request.POST['editNumeroOpere']

        cursor.execute('''
            UPDATE AUTORE
            SET nome = %s, cognome = %s, nazione = %s, dataNascita = %s, dataMorte = %s, tipo = %s, numeroOpere = %s
            WHERE codice = %s
        ''', (nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere, codice))
        conn.commit()

        return redirect('autore')

    cursor.execute('SELECT * FROM AUTORE WHERE codice = %s', (codice,))
    autore = cursor.fetchone()
    cursor.close()
    conn.close()

    return render(request, 'main/autore.html', {'autore': autore})

def delete_autore(request, codice):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM AUTORE WHERE codice = %s', (codice,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    return redirect('autore')
