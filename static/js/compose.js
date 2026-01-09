composer = document.getElementById('composer');

composer.addEventListener('input', 
    document.getElementById('char-count').innerHTML = 280-composer.value.length;
});
