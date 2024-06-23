var codiceToDelete = null;
var editFormId = null;

function nascondiModal(modal) {
    $(modal).modal('hide');
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


function mostraConfermaInserimento() {
    var form = document.getElementById('inserisciAutoreForm');
    if (form.checkValidity()) {
        impostaTipoCreate();
        $('#confermaModal').modal('show');
    } else {
        form.reportValidity();
    }
}

function confermaInserimento() {
    console.log("Invio modulo conferma inserimento"); // conferma log
    document.getElementById('inserisciAutoreForm').submit();
    $('#confermaModal').modal('hide');
}
$(document).ready(function() {
    impostaTipoCreate();
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
    $('.selectpicker').selectpicker();
});


// Modifica il codice per chiudere il modal di conferma
function confermaModifica() {
    if (editFormId !== null) {
        $('#editForm' + editFormId).submit();
        $('#editConfirmModal').modal('hide');
    }
}

var codiceToDelete = null;

var codiceToDelete = null;

function showDeleteConfirm(codice) {
    codiceToDelete = codice;
    var deleteForm = document.getElementById('deleteForm');
    deleteForm.action = '/delete_autore/' + codiceToDelete + '/';
    $('#deleteConfirmModal').modal('show');
}

$(document).ready(function() {
    impostaTipoCreate();
    
    // Inizializza il datepicker per tutti gli input datepicker
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
    $('.selectpicker').selectpicker();
});

function confermaCancellazione() {
    if (codiceToDelete !== null) {
        var form = document.createElement('form');
        form.method = 'POST';
        form.action = '/delete_autore/' + codiceToDelete + '/';
        
        var csrfToken = document.createElement('input');
        csrfToken.type = 'hidden';
        csrfToken.name = 'csrfmiddlewaretoken';
        csrfToken.value = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        form.appendChild(csrfToken);
        document.body.appendChild(form);
        form.submit();
    }
    $('#deleteConfirmModal').modal('hide');
}

$(document).ready(function() {
    impostaTipoCreate();
    
    // Inizializza il datepicker per tutti gli input datepicker
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
    $('.selectpicker').selectpicker();
});