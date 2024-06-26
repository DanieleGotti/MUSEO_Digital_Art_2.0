var codiceToDelete = null;  // Variabile per memorizzare il codice dell'autore da eliminare
var editFormId = null;  // Variabile per memorizzare l'ID del form di modifica

// Funzione per nascondere una modale
function nascondiModal(modal) {
    $(modal).modal('hide');
}

// Funzione per impostare il tipo (Vivo/Morto) durante la creazione
function impostaTipoCreate() {
    var dataMorte = document.getElementById('dataMortecreate').value;
    var tipo = document.getElementById('tipocreate');
    
    if (dataMorte) {
        tipo.value = 'Morto';
    } else {
        tipo.value = 'Vivo';
    }
}

// Funzione per impostare il tipo (Vivo/Morto) durante la modifica
function impostaTipoEdit(formId) {
    var dataMorteElement = document.getElementById('dataMorteedit' + formId);
    var tipoElement = document.getElementById('editTipo' + formId);

    if (dataMorteElement && tipoElement) {
        var dataMorte = dataMorteElement.value;
        if (dataMorte) {
            tipoElement.value = 'Morto';
        } else {
            tipoElement.value = 'Vivo';
        }
    }
}

// Funzione per mostrare o nascondere il form di modifica
function toggleEditForm(codice) {
    var formRow = document.getElementById('editFormRow' + codice);
    if (formRow.style.display === 'none' || formRow.style.display === '') {
        formRow.style.display = 'table-row';
    } else {
        formRow.style.display = 'none';
    }
}

// Funzione per mostrare la modale di creazione
function showCreateForm() {
    $('#createAuthorModal').modal('show');
}

// Funzione per validare le date di nascita e morte
function validateDateOfBirthAndDeath(birthDateId, deathDateId) {
    var birthDateStr = document.getElementById(birthDateId).value;
    var deathDateStr = document.getElementById(deathDateId).value;

    if (birthDateStr && deathDateStr) {
        var birthDate = moment(birthDateStr, "DD/MM/YYYY");
        var deathDate = moment(deathDateStr, "DD/MM/YYYY");

        if (deathDate.isBefore(birthDate)) {
            alert("La data di morte deve essere successiva alla data di nascita.");
            return false;
        }
    }
    return true;
}

// Funzione per mostrare la modale di conferma inserimento
function mostraConfermaInserimento() {
    var form = document.getElementById('inserisciAutoreForm');
    if (form.checkValidity()) {

        var isValid = validateDateOfBirthAndDeath('dataNascitacreate', 'dataMortecreate');
        if (isValid && document.getElementById('inserisciAutoreForm').checkValidity()) {
            impostaTipoCreate();
            $('#confermaModal').modal('show');
        } else {
            document.getElementById('inserisciAutoreForm').reportValidity();
        }
    }
}

// Funzione per mostrare la modale di conferma modifica
function mostraConfermaModifica(formId) {
    var isValid = validateDateOfBirthAndDeath('dataNascitaedit' + formId, 'dataMorteedit' + formId);
    if (isValid) {
        impostaTipoEdit(formId);
        editFormId = formId;
        $('#editConfirmModal').modal('show');
    }
}

// Funzione per confermare la modifica
function confermaModifica() {
    if (editFormId !== null) {
        $('#editForm' + editFormId).submit();
        $('#editConfirmModal').modal('hide');
    }
}

// Funzione per mostrare la modale di conferma cancellazione
function showDeleteConfirm(codice) {
    codiceToDelete = codice;
    var deleteForm = document.getElementById('deleteForm');
    deleteForm.action = '/delete_autore/' + codiceToDelete + '/';
    $('#deleteConfirmModal').modal('show');
}

// Inizializza le funzioni quando il documento è pronto
$(document).ready(function() {
    impostaTipoCreate();
    
    // Inizializza il datepicker per tutti gli input con classe datepicker
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
    $('.selectpicker').selectpicker();
});

// Funzione per confermare la cancellazione
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

// Inizializza le funzioni quando il documento è pronto
$(document).ready(function() {
    impostaTipoCreate();
    
    // Inizializza il datepicker per tutti gli input con classe datepicker
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
    $('.selectpicker').selectpicker();
});

// Funzione per confermare l'inserimento
function confermaInserimento() {
    console.log("Invio modulo conferma inserimento"); // conferma log
    document.getElementById('inserisciAutoreForm').submit();
    $('#confermaModal').modal('hide');
}

// Inizializza le funzioni quando il documento è pronto
$(document).ready(function() {
    impostaTipoCreate();
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'it'
    });
    $('.selectpicker').selectpicker();
});

// Imposta il padding del contenitore dei messaggi dopo il caricamento del documento
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.getElementById('messages');
    const contentContainer = document.getElementById('content-container');
    if (messages) {
        contentContainer.style.paddingTop = '1rem';
    } else {
        contentContainer.style.paddingTop = '2rem';
    }
});
