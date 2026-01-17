document.addEventListener('DOMContentLoaded', (_) => {

    composer = document.getElementById('composer');

    composer.addEventListener('input', (_) => { 
        document.getElementById('char-count').innerHTML = 280-composer.value.length;
    });

})
