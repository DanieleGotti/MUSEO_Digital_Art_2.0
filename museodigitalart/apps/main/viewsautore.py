from django.shortcuts import render, redirect
from django.db import connection
from datetime import datetime
from django.contrib import messages
import sqlite3
import re

def get_connection():
    return connection  # Usa il connection object fornito da Django

def convert_date(date_str):
    try:
        # Prova a convertire la data dal formato yyyy-mm-dd a dd/mm/yyyy
        return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d/%m/%Y')
    except (ValueError, TypeError):
        # Se fallisce, significa che la data è già nel formato dd/mm/yyyy o è None
        return date_str

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
    sort_by = request.GET.get('sort_by', 'AUTORE.codice')
    sort_order = request.GET.get('sort_order', 'asc')

    # Mantieni lo stato di mostra_crud
    mostra = request.session.get('mostra_crud', False)

    if request.method == 'POST' and 'toggle_crud' in request.POST:
        mostra = not mostra  # Inverti lo stato
        request.session['mostra_crud'] = mostra  # Salva lo stato nella sessione

    query = get_autore_query(codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere, nomeopera, sort_by, sort_order)
    cursor.execute(query)
    rows = cursor.fetchall()

    # Convert dates to dd/mm/yyyy format
    formatted_rows = []
    for row in rows:
        formatted_row = list(row)
        formatted_row[4] = convert_date(formatted_row[4])  # dataNascita
        formatted_row[5] = convert_date(formatted_row[5])  # dataMorte
        formatted_rows.append(tuple(formatted_row))

    cursor.close()
    conn.close()

    # Calcola le URL per l'ordinamento
    base_url = request.path
    params = request.GET.copy()
    params['sort_order'] = 'asc' if sort_order == 'desc' else 'desc'

    url_codice = f"{base_url}?sort_by=AUTORE.codice&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_nome = f"{base_url}?sort_by=AUTORE.nome&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_cognome = f"{base_url}?sort_by=AUTORE.cognome&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_nazione = f"{base_url}?sort_by=AUTORE.nazione&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_dataNascita = f"{base_url}?sort_by=AUTORE.dataNascita&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_dataMorte = f"{base_url}?sort_by=AUTORE.dataMorte&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_tipo = f"{base_url}?sort_by=AUTORE.tipo&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_numeroOpere = f"{base_url}?sort_by=AUTORE.numeroOpere&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"

    context = {
        'autori': formatted_rows,
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
        'url_codice': url_codice,
        'url_nome': url_nome,
        'url_cognome': url_cognome,
        'url_nazione': url_nazione,
        'url_dataNascita': url_dataNascita,
        'url_dataMorte': url_dataMorte,
        'url_tipo': url_tipo,
        'url_numeroOpere': url_numeroOpere,
    }

    return render(request, 'main/autore.html', context)


def get_autore_query(codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere, nomeopera, sort_by, sort_order):
    query = """
    SELECT AUTORE.codice, AUTORE.nome, AUTORE.cognome, AUTORE.nazione, 
           AUTORE.dataNascita, AUTORE.dataMorte, AUTORE.tipo, AUTORE.numeroOpere
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
        query += f" AND AUTORE.numeroOpere LIKE '%{numeroOpere}%'"
    if nomeopera:
        query = f"""
        SELECT DISTINCT AUTORE.codice, AUTORE.nome, AUTORE.cognome, AUTORE.nazione, 
               AUTORE.dataNascita, AUTORE.dataMorte, AUTORE.tipo, AUTORE.numeroOpere, OPERA.titolo AS nomeopera
        FROM AUTORE
        JOIN OPERA ON OPERA.autore = AUTORE.codice
        WHERE OPERA.titolo LIKE '%{nomeopera}%'
        """

    if sort_by and sort_order:
        if sort_by in ['AUTORE.dataNascita', 'AUTORE.dataMorte']:
            query += f" ORDER BY substr({sort_by}, 7, 4) || '-' || substr({sort_by}, 4, 2) || '-' || substr({sort_by}, 1, 2) {sort_order}"
        else:
            query += f" ORDER BY {sort_by} {sort_order}"

    return query

#query necessaria quando si vuole eseguire una query sulla tabella autore a partire dalla pagina di opera
def autore_opera(request, autore_codice):
    conn = get_connection()
    cursor = conn.cursor()

    codice = autore_codice
    nome = request.GET.get('nome', '')
    cognome = request.GET.get('cognome', '')
    nazione = request.GET.get('nazione', '')
    dataNascita = request.GET.get('dataNascita', '')
    dataMorte = request.GET.get('dataMorte', '')
    tipo = request.GET.get('tipo', '')
    numeroOpere = request.GET.get('numeroOpere', '')
    nomeopera = request.GET.get('nomeopera', '')
    sort_by = request.GET.get('sort_by', 'AUTORE.codice')
    sort_order = request.GET.get('sort_order', 'asc')

    # Mantieni lo stato di mostra_crud
    mostra = request.session.get('mostra_crud', False)

    if request.method == 'POST' and 'toggle_crud' in request.POST:
        mostra = not mostra  # Inverti lo stato
        request.session['mostra_crud'] = mostra  # Salva lo stato nella sessione

    # Costruzione della query SQL con i filtri
    query = """
    SELECT AUTORE.codice, AUTORE.nome, AUTORE.cognome, AUTORE.nazione, AUTORE.dataNascita, AUTORE.dataMorte, AUTORE.tipo, AUTORE.numeroOpere
    FROM AUTORE
    WHERE AUTORE.codice = ?
    """

    params = [autore_codice]

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
        if sort_by in ['AUTORE.dataNascita', 'AUTORE.dataMorte']:
            query += f" ORDER BY substr({sort_by}, 7, 4) || '-' || substr({sort_by}, 4, 2) || '-' || substr({sort_by}, 1, 2) {sort_order}"
        else:
            query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query, params)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Calcola le URL per l'ordinamento
    base_url = request.path
    params = request.GET.copy()
    params['sort_order'] = 'asc' if sort_order == 'desc' else 'desc'

    url_codice = f"{base_url}?sort_by=AUTORE.codice&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_nome = f"{base_url}?sort_by=AUTORE.nome&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_cognome = f"{base_url}?sort_by=AUTORE.cognome&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_nazione = f"{base_url}?sort_by=AUTORE.nazione&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_dataNascita = f"{base_url}?sort_by=AUTORE.dataNascita&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_dataMorte = f"{base_url}?sort_by=AUTORE.dataMorte&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_tipo = f"{base_url}?sort_by=AUTORE.tipo&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"
    url_numeroOpere = f"{base_url}?sort_by=AUTORE.numeroOpere&sort_order={params['sort_order']}&codice={codice}&nome={nome}&cognome={cognome}&nazione={nazione}&dataNascita={dataNascita}&dataMorte={dataMorte}&tipo={tipo}&numeroOpere={numeroOpere}&nomeopera={nomeopera}"

    context = {
        'autori': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'codice': autore_codice,
        'nome': nome,
        'cognome': cognome,
        'nazione': nazione,
        'dataNascita': dataNascita,
        'dataMorte': dataMorte,
        'tipo': tipo,
        'numeroOpere': numeroOpere,
        'nomeopera': nomeopera,
        'mostra': mostra,
        'url_codice': url_codice,
        'url_nome': url_nome,
        'url_cognome': url_cognome,
        'url_nazione': url_nazione,
        'url_dataNascita': url_dataNascita,
        'url_dataMorte': url_dataMorte,
        'url_tipo': url_tipo,
        'url_numeroOpere': url_numeroOpere,
    }

    return render(request, 'main/autore.html', context)


def get_connection():
    return sqlite3.connect('db.sqlite3')




def create_autore(request):
    if request.method == 'POST':
        codicecreate = request.POST['codicecreate']
        nomecreate = request.POST['nomecreate']
        cognomecreate = request.POST['cognomecreate']
        nazionecreate = request.POST['nazionecreate']
        dataNascitacreate = request.POST['dataNascitacreate']
        dataMortecreate = request.POST.get('dataMortecreate', '')  # Default vuoto se non c'è
        tipocreate = request.POST['tipocreate']
        numeroOperecreate = request.POST.get('numeroOperecreate', '0')  # default '0'

        # Validazione dei campi richiesti
        if not (codicecreate and nomecreate and cognomecreate and nazionecreate and dataNascitacreate and tipocreate):
            messages.error(request, 'Tutti i campi tranne Data Morte sono obbligatori.')
            return redirect('autore')

        # Verifica che il codice contenga solo cifre e sia superiore a 100
        if not re.match(r'^[0-9]+$', codicecreate):
            messages.error(request, 'Il codice deve essere un numero contenente solo cifre.')
            return redirect('autore')

        # Converti date 
        try:
            dataNascitacreate = datetime.strptime(dataNascitacreate, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            messages.error(request, 'Formato Data Nascita non valido.')
            return redirect('autore')

        try:
            if dataMortecreate:
                dataMortecreate = datetime.strptime(dataMortecreate, '%d/%m/%Y').strftime('%Y-%m-%d')
            else:
                dataMortecreate = None
        except ValueError:
            messages.error(request, 'Formato Data Morte non valido.')
            return redirect('autore')

        conn = get_connection()
        cursor = conn.cursor()

        # Controllo se il codice esiste già
        cursor.execute('SELECT COUNT(*) FROM AUTORE WHERE codice = ?', (codicecreate,))
        if cursor.fetchone()[0] > 0:
            messages.error(request, 'Il codice esiste già.')
            cursor.close()
            conn.close()
            return redirect('autore')

        cursor.execute('''
            INSERT INTO AUTORE (codice, nome, cognome, nazione, dataNascita, dataMorte, tipo, numeroOpere)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (codicecreate, nomecreate, cognomecreate, nazionecreate, dataNascitacreate, dataMortecreate or '', tipocreate, numeroOperecreate))
        conn.commit()
        cursor.close()
        conn.close()

        messages.success(request, 'Autore inserito con successo.')
        return redirect('autore')

    return render(request, 'main/autore.html')

#funzione per la modifica
def update_autore(request, codice):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        editNome = request.POST['editNome']
        editCognome = request.POST['editCognome']
        editNazione = request.POST['editNazione']
        editDataNascita = request.POST.get('editDataNascita', None)
        editDataMorte = request.POST.get('editDataMorte', None)
        editTipo = request.POST['editTipo']
        editNumeroOpere = request.POST['editNumeroOpere']

       
        cursor.execute('SELECT dataNascita, dataMorte FROM AUTORE WHERE codice = ?', (codice,))
        data = cursor.fetchone()
        dataNascita, dataMorte = data[0], data[1]

        # Converti data
        if editDataNascita:
            try:
                editDataNascita = datetime.strptime(editDataNascita, '%d/%m/%Y').strftime('%Y-%m-%d')
            except ValueError:
                editDataNascita = dataNascita
        else:
            editDataNascita = dataNascita

        if editDataMorte:
            try:
                editDataMorte = datetime.strptime(editDataMorte, '%d/%m/%Y').strftime('%Y-%m-%d')
            except ValueError:
                editDataMorte = dataMorte
        else:
            editDataMorte = dataMorte

        cursor.execute('''
            UPDATE AUTORE
            SET nome = ?, cognome = ?, nazione = ?, dataNascita = ?, dataMorte = ?, tipo = ?, numeroOpere = ?
            WHERE codice = ?
        ''', (editNome, editCognome, editNazione, editDataNascita, editDataMorte, editTipo, editNumeroOpere, codice))
        conn.commit()
        messages.success(request, 'Autore modificato con successo.')
        return redirect('autore')

    cursor.execute('SELECT * FROM AUTORE WHERE codice = ?', (codice,))
    autore = cursor.fetchone()

    
    if autore[4]:
        autore = list(autore)
        autore[4] = convert_date(autore[4])
    if autore[5]:
        autore = list(autore)
        autore[5] = convert_date(autore[5])

    cursor.close()
    conn.close()

    return render(request, 'main/autore.html', {'autore': autore})

#funzione di eliminazione da db
def delete_autore(request, codice):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM AUTORE WHERE codice = ?', (codice,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    messages.success(request, 'Autore eliminato con successo.')
    return redirect('autore')
