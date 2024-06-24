from django.shortcuts import render
import sqlite3

def sala(request):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
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
          query = f"""
                    SELECT DISTINCT SALA.numero, SALA.nome, SALA.superficie, SALA.numeroOpere, SALA.temaSala, TEMA.descrizione, OPERA.titolo AS nomeopera
                    FROM SALA
                    LEFT JOIN TEMA ON SALA.temaSala = TEMA.codice
                    LEFT JOIN OPERA ON OPERA.espostaInSala = SALA.numero
                    WHERE OPERA.titolo LIKE '%{nomeopera}%'
                    """

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Calcola le URL per l'ordinamento
    base_url = request.path
    params = request.GET.copy()
    params['sort_order'] = 'asc' if sort_order == 'desc' else 'desc'

    url_numero = f"{base_url}?sort_by=numero&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_nome = f"{base_url}?sort_by=nome&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_superficie = f"{base_url}?sort_by=superficie&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_numeroOpere = f"{base_url}?sort_by=numeroOpere&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_temaSala = f"{base_url}?sort_by=temaSala&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_descrizione = f"{base_url}?sort_by=descrizione&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_nomeopera = f"{base_url}?sort_by=nomeopera&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"

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
        'nomeopera': nomeopera,
        'url_numero': url_numero,
        'url_nome': url_nome,
        'url_superficie': url_superficie,
        'url_numeroOpere': url_numeroOpere,
        'url_temaSala': url_temaSala,
        'url_descrizione': url_descrizione,
        'url_nomeopera': url_nomeopera
    }

    return render(request, 'main/sala.html', context)


def sala_opera(request, sala_numero):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    numero = sala_numero
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
    WHERE SALA.numero = ?
    """

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
                WHERE SALA.numero = ? AND OPERA.titolo LIKE '%{nomeopera}%'
                """

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query, (sala_numero,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Calcola le URL per l'ordinamento
    base_url = request.path
    params = request.GET.copy()
    params['sort_order'] = 'asc' if sort_order == 'desc' else 'desc'

    url_numero = f"{base_url}?sort_by=numero&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_nome = f"{base_url}?sort_by=nome&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_superficie = f"{base_url}?sort_by=superficie&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_numeroOpere = f"{base_url}?sort_by=numeroOpere&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_temaSala = f"{base_url}?sort_by=temaSala&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_descrizione = f"{base_url}?sort_by=descrizione&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_nomeopera = f"{base_url}?sort_by=nomeopera&sort_order={params['sort_order']}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&temaSala={temaSala}&descrizione={descrizione}&nomeopera={nomeopera}"

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
        'nomeopera': nomeopera,
        'url_numero': url_numero,
        'url_nome': url_nome,
        'url_superficie': url_superficie,
        'url_numeroOpere': url_numeroOpere,
        'url_temaSala': url_temaSala,
        'url_descrizione': url_descrizione,
        'url_nomeopera': url_nomeopera
    }

    return render(request, 'main/sala.html', context)

def sala_tema(request, tema_codice):
    # Connessione al database SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Recupero dei parametri di filtro
    numero = request.GET.get('numero', '')
    nome = request.GET.get('nome', '')
    superficie = request.GET.get('superficie', '')
    numeroOpere = request.GET.get('numeroOpere', '')
    descrizione = request.GET.get('descrizione', '')
    nomeopera = request.GET.get('nomeopera', '')
    sort_by = request.GET.get('sort_by', 'numero')
    sort_order = request.GET.get('sort_order', 'asc')

    # Costruzione della query SQL con i filtri
    query = """
    SELECT DISTINCT SALA.numero, SALA.nome, SALA.superficie, SALA.numeroOpere, SALA.temaSala, TEMA.descrizione
    FROM SALA
    LEFT JOIN TEMA ON SALA.temaSala = TEMA.codice
    WHERE SALA.temaSala = ?
    """

    if numero:
        query += f" AND SALA.numero = '{numero}'"
    if nome:
        query += f" AND SALA.nome LIKE '%{nome}%'"
    if superficie:
        query += f" AND SALA.superficie LIKE '%{superficie}%'"
    if numeroOpere:
        query += f" AND SALA.numeroOpere LIKE '%{numeroOpere}%'"
    if descrizione:
        query += f" AND TEMA.descrizione LIKE '%{descrizione}%'"
    if nomeopera:
        query = """
                SELECT DISTINCT SALA.numero, SALA.nome, SALA.superficie, SALA.numeroOpere, SALA.temaSala, TEMA.descrizione, OPERA.titolo AS nomeopera
                FROM SALA
                LEFT JOIN TEMA ON SALA.temaSala = TEMA.codice
                LEFT JOIN OPERA ON OPERA.espostaInSala = SALA.numero
                WHERE SALA.temaSala = ? AND OPERA.titolo LIKE '%{nomeopera}%'
                """

    if sort_by and sort_order:
        query += f" ORDER BY {sort_by} {sort_order}"

    cursor.execute(query, (tema_codice,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Calcola le URL per l'ordinamento
    base_url = request.path
    params = request.GET.copy()
    params['sort_order'] = 'asc' if sort_order == 'desc' else 'desc'

    url_numero = f"{base_url}?sort_by=numero&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_nome = f"{base_url}?sort_by=nome&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_superficie = f"{base_url}?sort_by=superficie&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_numeroOpere = f"{base_url}?sort_by=numeroOpere&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_descrizione = f"{base_url}?sort_by=descrizione&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&descrizione={descrizione}&nomeopera={nomeopera}"
    url_nomeopera = f"{base_url}?sort_by=nomeopera&sort_order={params['sort_order']}&numero={numero}&nome={nome}&superficie={superficie}&numeroOpere={numeroOpere}&descrizione={descrizione}&nomeopera={nomeopera}"

    context = {
        'sale': rows,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'numero': numero,
        'nome': nome,
        'superficie': superficie,
        'numeroOpere': numeroOpere,
        'temaSala': tema_codice,
        'descrizione': descrizione,
        'nomeopera': nomeopera,
        'url_numero': url_numero,
        'url_nome': url_nome,
        'url_superficie': url_superficie,
        'url_numeroOpere': url_numeroOpere,
        'url_descrizione': url_descrizione,
        'url_nomeopera': url_nomeopera
    }

    return render(request, 'main/sala.html', context)
