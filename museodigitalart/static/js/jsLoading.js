// Mostra o nasconde la schermata di caricamento, ogni pagina è mostrata solo se completamente caricata
window.addEventListener('load', function () {
    var loadingOverlay = document.querySelector('.caricamento');
    var content = document.getElementById('body');
  
    // Nascondi l'overlay di caricamento con animazione
    loadingOverlay.classList.add('hidden');
  
    // Mostra il contenuto
    content.style.display = 'block';
  
    // Rimuovi completamente l'overlay dopo l'animazione
    setTimeout(function() {
      loadingOverlay.style.display = 'none';
    }, 500); // La durata deve corrispondere alla durata dell'animazione CSS
  });