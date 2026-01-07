let sidebar_toggle = document.getElementById('toggle-sidebar-container');
let sidebar = document.getElementById('sidebar');

sidebar_toggle.addEventListener('click', (_) => {
    sidebar.classList.toggle('collapsed');
});