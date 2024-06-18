// Sostituisce le .gif ai .png della navbar se c'è hover
function animateIcon(element) {
    var img = element.querySelector('img');
    var srcImg = img.src;
  
    var newGif = srcImg.replace('Statica.png', '.gif');
    var newPng = srcImg.replace('.gif', 'Statica.png');
  
    if (srcImg.includes('.png')) {
      img.src = newGif;
    }
  
    if (srcImg.includes('.gif')) {
      img.src = newPng;
    }
  }
  
  // Cambia colore del background alle icone della navbar se c'è hover
  document.addEventListener('DOMContentLoaded', function() {
    let currentPage = window.location.pathname.split("/").pop();
    let elements = document.getElementsByClassName('navItem');
    const color = '#F76E11';
  
    if (elements.length === 0) {
      console.log("Nessun elemento trovato con la classe 'navItem'");
      return;
    }
  
    switch (currentPage) {
      case 'index.php':
        elements[0].style.backgroundColor = color;
        break;
      case 'tema.php':
        elements[1].style.backgroundColor = color;
        break;
      case 'sala.php':
        elements[2].style.backgroundColor = color;
        break;
      case 'opera.php':
        elements[3].style.backgroundColor = color;
        break;
      case 'autore.php':
        elements[4].style.backgroundColor = color;
        break;
      }
  });
  