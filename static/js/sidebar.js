// Grabbing the sidebar
async function set_sidebar() {
    try {
        const sidebar_url = '/sidebar';
        const response = await fetch(sidebar_url);

        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }

        const html = await response.text();
        // Got the html data, assign it
        document.getElementById('sidebar').innerHTML = html;
    } catch (err) {
        alert('Fetch failed: ' + err.message);
        console.error(err);
        return undefined;
    }
}

async function sidebar_functions() {
    await set_sidebar();

    // Functionality goes here
    let sidebar_toggle = document.getElementById('toggle-sidebar-container');
    let sidebar = document.getElementById('sidebar');

    let dropdown = document.getElementById('dropdown-btn-container');
    let dropdown_hide = document.getElementById('sidebar-dropdown-hide')

    let up_arrow = document.getElementById('up_arrow')
    let down_arrow = document.getElementById('down_arrow')

    let collapsed = localStorage.getItem('collapsed_sidebar') === 'true'

    if(collapsed){
        sidebar.classList.toggle("collapsed")
    }


    sidebar_toggle.addEventListener('click', (_) => {
        sidebar.classList.toggle('collapsed');
        localStorage.setItem('collapsed_sidebar', collapsed ? 'true' : 'false')
    });

    dropdown.addEventListener('click', (_) => {
        dropdown_hide.classList.toggle('collapsed');

        up_arrow.classList.toggle('hidden')
        down_arrow.classList.toggle('hidden')
    });
}

async function check_login_status(){
    try{

    let response = await fetch('/api/check-login')
    let data = await response.json()

    let pre_login = document.getElementById('pre-login')
    let post_login = document.getElementById('post-login')


    if (data.login){
        pre_login.classList.add('hidden')

        post_login.classList.remove('hidden')
    } else {
        pre_login.classList.remove('hidden')

        post_login.classList.add('hidden')


    }

    } catch (err) {
        console.error(err)
    }
}


document.addEventListener('DOMContentLoaded', (_) => {
    sidebar_functions();
    check_login_status();   
})

