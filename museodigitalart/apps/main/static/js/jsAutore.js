var codiceToDelete = null;
var editFormId = null;

function nascondiModal(modal) {
    $(modal).modal('hide');
}

function showDeleteConfirm(codice) {
    codiceToDelete = codice;
    $('#deleteConfirmModal').modal('show');
}

function confermaCancellazione() {
    if (codiceToDelete !== null) {
        $.ajax({
            type: "POST",
            url: "{% url 'delete_autore' 0 %}".replace('0', codiceToDelete),
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                console.log("Autore eliminato con successo!");
                window.location.reload();
            },
            error: function(xhr, status, error) {
                console.error("Errore durante la cancellazione dell'autore:", error);
            }
        });
    }
    $('#deleteConfirmModal').modal('hide');
}

function impostaTipoCreate() {
    var dataMorte = document.getElementById('dataMortecreate').value;
    var tipo = document.getElementById('tipocreate');
    
    if (dataMorte) {
        tipo.value = 'Morto';
    } else {
        tipo.value = 'Vivo';
    }
}

function mostraConfermaInserimento() {
    impostaTipoCreate(); // Imposta il tipo prima di mostrare la conferma
    $('#confermaModal').modal('show');
}

function mostraConfermaInserimento() {
    // Controlla che tutti i campi obbligatori siano riempiti
    var form = document.getElementById('inserisciAutoreForm');
    if (form.checkValidity()) {
        impostaTipoCreate(); // Imposta il tipo prima di mostrare la conferma
        $('#confermaModal').modal('show');
    } else {
        // Se non tutti i campi sono riempiti, mostra un messaggio di errore
        form.reportValidity();
    }
}


function impostaTipoEdit(formId) {
    var dataMorte = document.getElementById('editDataMorte' + formId).value;
    var tipo = document.createElement('input');
    tipo.type = 'hidden';
    tipo.name = 'editTipo';
    tipo.id = 'editTipo' + formId;
    if (dataMorte) {
        tipo.value = 'Morto';
    } else {
        tipo.value = 'Vivo';
    }
    document.getElementById('editForm' + formId).appendChild(tipo);
}

function mostraConfermaModifica(formId) {
    impostaTipoEdit(formId); // Imposta il tipo prima di mostrare la conferma
    editFormId = formId;
    $('#editConfirmModal').modal('show');
}

function confermaModifica() {
    if (editFormId !== null) {
        $('#editForm' + editFormId).submit();
        $('#editConfirmModal').modal('hide');
    }
}

function toggleEditForm(codice) {
    var formRow = document.getElementById('editFormRow' + codice);
    if (formRow.style.display === 'none' || formRow.style.display === '') {
        formRow.style.display = 'table-row';
    } else {
        formRow.style.display = 'none';
    }
}

function showCreateForm() {
    $('#createAuthorModal').modal('show');
}

// Chiamare impostaTipoCreate anche quando la pagina è caricata, per impostare correttamente il valore iniziale
$(document).ready(function() {
    impostaTipoCreate();

    // Inizializza il datepicker per tutti gli input datepicker
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
});
