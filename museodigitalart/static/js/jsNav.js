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
    var currentPage = window.location.pathname.split("/").filter(Boolean).pop() || "home";
    var elements = document.getElementsByClassName('navItem');
    const color = '#F76E11';
  
    if (elements.length === 0) {
      return;
    }

    switch (currentPage) {
      case 'home':
        elements[0].style.backgroundColor = color;
        break;
      case 'tema':
        elements[1].style.backgroundColor = color;
        break;
      case 'sala':
        elements[2].style.backgroundColor = color;
        break;
      case 'opera':
        elements[3].style.backgroundColor = color;
        break;
      case 'autore':
        elements[4].style.backgroundColor = color;
        break;
      default:
        console.log("Pagina non trovata nel switch case");
    }
  });
  