// Inizialmente i filtri sono visibili a sinistra
let isExpanded = true;

// Se premuto il bottone filtri si sparisce, se ripremuto riappare
function moveFilters() {
  const box = document.getElementById('filtri');
  const table = document.getElementById('result');

  if (isExpanded) {
      box.style.width = '0rem';
      table.style.marginLeft = '4rem';
  } else {
      box.style.width = '12rem';
      table.style.marginLeft = '14rem';
  }
  isExpanded = !isExpanded;
}

// Cambia classe agli input in modo che il placeHolder cambi posizione
document.addEventListener('DOMContentLoaded', function () {
  const inputs = document.querySelectorAll('.input');

  inputs.forEach(function (input) {
    input.addEventListener('input', function () {
      if (input.value !== '') {
        input.classList.add('notEmpty');
      } else {
        input.classList.remove('notEmpty');
      }
    });
  });
});

// Cambia classe agli inputPop in modo che il placeHolder cambi posizione
document.addEventListener('DOMContentLoaded', function () {
  const inputs = document.querySelectorAll('.input');

  inputs.forEach(function (input) {
    if (input.value !== '') {
      input.classList.add('notEmpty');
    }

    input.addEventListener('input', function () {
      if (input.value !== '') {
        input.classList.add('notEmpty');
      } else {
        input.classList.remove('notEmpty');
      }
    });
  });
});
