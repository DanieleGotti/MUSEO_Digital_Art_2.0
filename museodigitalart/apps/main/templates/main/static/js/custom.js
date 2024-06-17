function mostraConferma() {
    $('#confermaModal').modal('show');
    return false; // Previene l'invio del form finché l'utente non conferma
}

function confermaInserimento() {
    $('#inserisciAutoreForm').off('submit').submit(); // Rimuove il gestore di submit e invia il form
}
