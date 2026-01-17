function toggle_show_password() {
    let password_input = document.getElementById('password');

    password_input.type = (password_input.type === 'password' ? 'text' : 'password');
}

function toggle_useroptions() {
    let options = document.getElementById('password');
    
    options.style.display === 'none' ? 'block' : 'none';
}
