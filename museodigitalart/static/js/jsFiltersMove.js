// Funzione che controlla i movomenti dei placeHolder degli input
document.addEventListener('DOMContentLoaded', function () {
  const inputs = document.querySelectorAll('.input');

  function checkInputValue(input) {
    if (input.value !== '') {
      input.classList.add('notEmpty');
    } else {
      input.classList.remove('notEmpty');
    }
  }

  // Controlla tutti gli input all'inizio
  inputs.forEach(function (input) {
    checkInputValue(input);
  });

  // Aggiunge eventi per monitorare cambiamenti di valore
  inputs.forEach(function (input) {
    input.addEventListener('input', function () {
      checkInputValue(input);
    });

    input.addEventListener('change', function () {
      checkInputValue(input);
    });

    // Se l'input è un datepicker di Bootstrap
    if (input.classList.contains('datepicker')) {
      $(input).datepicker()
        .on('changeDate', function () {
          checkInputValue(input);
        });
    }
  });
});




