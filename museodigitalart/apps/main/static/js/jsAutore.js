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

function mostraConfermaModifica(formId) {
    var isValid = validateDateOfBirthAndDeath('dataNascitaedit' + formId, 'dataMorteedit' + formId);
    if (isValid) {
        impostaTipoEdit(formId);
        editFormId = formId;
        $('#editConfirmModal').modal('show');
    }
}

function confermaModifica() {
    if (editFormId !== null) {
        $('#editForm' + editFormId).submit();
        $('#editConfirmModal').modal('hide');
    }
}

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

//Modal di conferma
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