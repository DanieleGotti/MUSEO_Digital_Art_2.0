// static/js/jsFooter.js
document.addEventListener('DOMContentLoaded', function() {
    let currentPage = window.location.pathname.split("/").pop();
    let footer = document.getElementById('footer');
    if (footer && currentPage !== 'home.html') {
      footer.classList.add('fixed');
    }
  });
  